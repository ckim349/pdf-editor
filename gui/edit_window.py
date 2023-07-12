from PySide6.QtCore import QRectF
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QComboBox, QLineEdit
from PySide6.QtPdf import QPdfPageNavigator
from scripts.pagehelper import add_page, rotate, delete_page, crop, rearrange, get_size
from edit_window_pdf import EditWindowPdf

class BaseEditWindow(QWidget):
    def __init__(self, pdf_tab):
        super().__init__()
        self.pdf_tab = pdf_tab
        self.edit_window_pdf = EditWindowPdf()

        back_page_button = QPushButton("<")
        page_number = QLabel("1/2")
        next_page_button = QPushButton(">")

        self.pdf_view_layout = QVBoxLayout()
        pdf_buttons_layout = QHBoxLayout()
        self.pdf_view_layout.addLayout(pdf_buttons_layout)
        self.pdf_view_layout.addWidget(self.edit_window_pdf)
        self.edit_window_pdf.open(self.pdf_tab.reload_reference)

        self.editing_layout = QVBoxLayout()
        self.page_label = QLabel("Choose page:")
        self.page_select = QComboBox()
        self.update_page_select()

        self.editing_layout.addWidget(self.page_label)
        self.editing_layout.addWidget(self.page_select)

        main_layout = QHBoxLayout()
        main_layout.addLayout(self.editing_layout)
        main_layout.addLayout(self.pdf_view_layout)

        pdf_buttons_layout.addWidget(back_page_button)
        pdf_buttons_layout.addWidget(page_number)
        pdf_buttons_layout.addWidget(next_page_button)

        self.setLayout(main_layout)

    def update_page_select(self):
        self.page_select.clear()
        for i in range(self.pdf_tab.pdf_document.pageCount()):
            self.page_select.addItem(str(i + 1))


class CropEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__(pdf_tab)
        self.setWindowTitle("Crop")
        self.pdf_tab = pdf_tab

        self.page_bounds = QLabel()
        self.page_select.currentIndexChanged.connect(self.update_page_bounds)
        self.editing_layout.addWidget(self.page_bounds)

        self.editing_layout.addWidget(QLabel("Lower left x: "))
        self.lower_left_x = QLineEdit("0")
        self.editing_layout.addWidget(self.lower_left_x)
        self.editing_layout.addWidget(QLabel("Lower left y: "))
        self.lower_left_y = QLineEdit("0")
        self.editing_layout.addWidget(self.lower_left_y)
        self.editing_layout.addWidget(QLabel("Upper right x: "))
        self.upper_right_x = QLineEdit(str(self.x))
        self.editing_layout.addWidget(self.upper_right_x)
        self.editing_layout.addWidget(QLabel("Upper right y: "))
        self.upper_right_y = QLineEdit(str(self.y))
        self.editing_layout.addWidget(self.upper_right_y)

        self.update_page_bounds()

        crop_button = QPushButton("Crop dat")
        self.editing_layout.addWidget(crop_button)
        crop_button.clicked.connect(self.crop_button_clicked)

    def crop_button_clicked(self):
        crop(self.pdf_tab.current_pdf[8:], float(self.page_select.currentText()), float(self.lower_left_x.text()), float(self.lower_left_y.text()), float(self.upper_right_x.text()), float(self.upper_right_y.text()))
        self.pdf_tab.open(self.pdf_tab.reload_reference)
        self.edit_window_pdf.open(self.pdf_tab.reload_reference)
        # self.pdf_tab.history.undo_stack.append()

    def update_page_bounds(self):
        current_page = int(self.page_select.currentText())
        self.x, self.y = get_size(self.pdf_tab.current_pdf[8:], current_page)
        self.page_bounds.setText(f"Page {current_page} bounds: {'{:.2f}'.format(self.x), '{:.2f}'.format(self.y)}")
        self.upper_right_x.setText(str('{:.2f}'.format(self.x)))
        self.upper_right_y.setText(str('{:.2f}'.format(self.y)))


class RotateEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__(pdf_tab)
        self.setWindowTitle("Rotate")
        self.pdf_tab = pdf_tab

        rotate_button = QPushButton("Rotate dat")
        self.editing_layout.addWidget(rotate_button)
        rotate_button.clicked.connect(self.rotate_button_clicked)

    def rotate_button_clicked(self):
        # Temporarily set to page 1
        rotate(self.pdf_tab.current_pdf[8:], int(self.page_select.currentText()))
        self.pdf_tab.open(self.pdf_tab.reload_reference)
        self.edit_window_pdf.open(self.pdf_tab.reload_reference)
        self.pdf_tab.history.undo_stack.append(("rotate", 1))


class AddPageEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__(pdf_tab)
        self.setWindowTitle("Add Page")
        self.pdf_tab = pdf_tab

        add_page_button = QPushButton("Add Page dat")
        self.editing_layout.addWidget(add_page_button)
        add_page_button.clicked.connect(self.add_page_button_clicked)

    def add_page_button_clicked(self):
        add_page(self.pdf_tab.current_pdf[8:], int(self.page_select.currentText()))
        self.pdf_tab.open(self.pdf_tab.reload_reference)
        self.edit_window_pdf.open(self.pdf_tab.reload_reference)
        self.update_page_select()
        self.pdf_tab.history.undo_stack.append(("add", 1))


class DeletePageEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__(pdf_tab)
        self.setWindowTitle("Delete Page")
        self.pdf_tab = pdf_tab

        delete_page_button = QPushButton("Delete Page dat")
        self.editing_layout.addWidget(delete_page_button)
        delete_page_button.clicked.connect(self.delete_page_button_clicked)

    def delete_page_button_clicked(self):
        delete_page(self.pdf_tab.current_pdf[8:], int(self.page_select.currentText()))
        self.pdf_tab.open(self.pdf_tab.reload_reference)
        self.edit_window_pdf.open(self.pdf_tab.reload_reference)
        self.update_page_select()
        self.pdf_tab.history.undo_stack.append(("delete", 1))


class RearrangeEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__(pdf_tab)
        self.setWindowTitle("Rearrange Pages")
        self.pdf_tab = pdf_tab

        self.new_page_label = QLabel("Choose page to swap with:")
        self.new_page_select = QComboBox()
        self.update_new_page_select()

        self.editing_layout.addWidget(self.new_page_label)
        self.editing_layout.addWidget(self.new_page_select)

        rearrange_button = QPushButton("Rearrange Pages dat")
        self.editing_layout.addWidget(rearrange_button)
        rearrange_button.clicked.connect(self.rearrange_button_clicked)

    def rearrange_button_clicked(self):
        rearrange(self.pdf_tab.current_pdf[8:], int(self.page_select.currentText()), int(self.new_page_select.currentText()))
        self.pdf_tab.open(self.pdf_tab.reload_reference)
        self.edit_window_pdf.open(self.pdf_tab.reload_reference)
        self.update_page_select()
        self.update_new_page_select()
        self.pdf_tab.history.undo_stack.append(("rearrange", 1, 2))

    def update_new_page_select(self):
        self.new_page_select.clear()
        for i in range(self.pdf_tab.pdf_document.pageCount()):
            self.new_page_select.addItem(str(i + 1))
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGridLayout
from scripts.pagehelper import add_page, rotate, delete_page, crop, rearrange

class BaseEditWindow(QWidget):
    def __init__(self):
        super().__init__()

        grid_layout = QGridLayout()

        back_page_button = QPushButton("<")
        page_number = QLabel("1/2")
        next_page_button = QPushButton(">")

        grid_layout.addWidget(back_page_button,3,3)
        grid_layout.addWidget(page_number,3,4)
        grid_layout.addWidget(next_page_button,3,5)

        self.setLayout(grid_layout)

class CropEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__()
        self.setWindowTitle("Crop")
        self.pdf_tab = pdf_tab

        crop_button = QPushButton("Crop dat")
        self.layout().addWidget(crop_button)
        crop_button.clicked.connect(self.crop_button_clicked)

    def crop_button_clicked(self):
        # Temporarily set to page 1
        crop(self.pdf_tab.current_pdf[8:], 1)
        self.pdf_tab.open(self.pdf_tab.reload_reference)


class RotateEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__()
        self.setWindowTitle("Rotate")
        self.pdf_tab = pdf_tab

        rotate_button = QPushButton("Rotate dat")
        self.layout().addWidget(rotate_button)
        rotate_button.clicked.connect(self.rotate_button_clicked)

    def rotate_button_clicked(self):
        # Temporarily set to page 1
        rotate(self.pdf_tab.current_pdf[8:], 1)
        self.pdf_tab.open(self.pdf_tab.reload_reference)

class AddPageEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__()
        self.setWindowTitle("Add Page")
        self.pdf_tab = pdf_tab

        add_page_button = QPushButton("Add Page dat")
        self.layout().addWidget(add_page_button)
        add_page_button.clicked.connect(self.add_page_button_clicked)

    def add_page_button_clicked(self):
        # Temporarily set to page 1
        add_page(self.pdf_tab.current_pdf[8:], 1)
        self.pdf_tab.open(self.pdf_tab.reload_reference)

class DeletePageEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__()
        self.setWindowTitle("Delete Page")
        self.pdf_tab = pdf_tab

        delete_page_button = QPushButton("Delete Page dat")
        self.layout().addWidget(delete_page_button)
        delete_page_button.clicked.connect(self.delete_page_button_clicked)

    def delete_page_button_clicked(self):
        # Temporarily set to page 1
        delete_page(self.pdf_tab.current_pdf[8:], 1)
        self.pdf_tab.open(self.pdf_tab.reload_reference)

class RearrangeEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__()
        self.setWindowTitle("Rearrange Pages")
        self.pdf_tab = pdf_tab

        rearrange_button = QPushButton("Rearrange Pages dat")
        self.layout().addWidget(rearrange_button)
        rearrange_button.clicked.connect(self.rearrange_button_clicked)

    def rearrange_button_clicked(self):
        # Temporarily set to page 1
        rearrange(self.pdf_tab.current_pdf[8:], 1, 2)
        self.pdf_tab.open(self.pdf_tab.reload_reference)
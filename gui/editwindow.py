from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGridLayout
from scripts.pagehelper import rotate

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

class DeletePageEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__()
        self.setWindowTitle("Delete Page")

class RearrangePageEditWindow(BaseEditWindow):
    def __init__(self, pdf_tab):
        super().__init__()
        self.setWindowTitle("Rearrange Pages")
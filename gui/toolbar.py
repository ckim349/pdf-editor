from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QToolBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QDialog
from PySide6.QtCore import QSize
from editwindow import RotateEditWindow
from scripts.pagehelper import add_page, delete_page, rotate, crop, rearrange


class ToolBar(QToolBar):
    def __init__(self, pdf_tab):
        super().__init__()
        self.pdf_tab = pdf_tab
        self.editwindow = None

        self.setIconSize(QSize(20, 20))
        self.addAction("&Print")
        self.addAction("&Find")
        self.addSeparator()

        self.addAction("&Zoom out")
        self.addAction("&Zoom in")
        zoom_combo_box = QComboBox()
        zoom_combo_box.addItem("50%")
        zoom_combo_box.addItem("75%")
        zoom_combo_box.addItem("100%")
        zoom_combo_box.addItem("125%")
        zoom_combo_box.addItem("150%")
        zoom_combo_box.addItem("175%")
        zoom_combo_box.addItem("200%")
        self.addWidget(zoom_combo_box)
        self.addSeparator()

        self.addAction("&Crop")
        rotate_action = self.addAction("&Rotate page")
        rotate_action.triggered.connect(self.rotate_triggered)
        self.addAction("&Add page")
        self.addAction("&Delete page")
        self.addAction("&Rearrange pages")
        more_tools_combo_box = QComboBox()
        more_tools_combo_box.addItem("More tools")
        more_tools_combo_box.addItem("Combine pdfs")
        more_tools_combo_box.addItem("Sign forms")
        more_tools_combo_box.addItem("Compress file")
        self.addWidget(more_tools_combo_box)

    def rotate_triggered(self):
        if not self.editwindow:
            self.editwindow = RotateEditWindow()
        self.editwindow.resize(650, 400)
        self.editwindow.show()
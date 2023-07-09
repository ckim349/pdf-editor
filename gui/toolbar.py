from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QToolBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QDialog
from PySide6.QtCore import QSize
from edit_window import RotateEditWindow, CropEditWindow, AddPageEditWindow, DeletePageEditWindow, RearrangeEditWindow
from scripts.pagehelper import add_page, delete_page, rotate, crop, rearrange


class ToolBar(QToolBar):
    def __init__(self, pdf_tab):
        super().__init__()
        self.pdf_tab = pdf_tab
        self.edit_window = None
        self.active_edit = None

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

        crop_action = self.addAction("&Crop")
        crop_action.triggered.connect(self.crop_triggered)

        rotate_action = self.addAction("&Rotate page")
        rotate_action.triggered.connect(self.rotate_triggered)

        add_page_action = self.addAction("&Add page")
        add_page_action.triggered.connect(self.add_page_triggered)

        delete_page_action = self.addAction("&Delete page")
        delete_page_action.triggered.connect(self.delete_page_triggered)

        rearrange_action = self.addAction("&Rearrange pages")
        rearrange_action.triggered.connect(self.rearrange_triggered)

        more_tools_combo_box = QComboBox()
        more_tools_combo_box.addItem("More tools")
        more_tools_combo_box.addItem("Combine pdfs")
        more_tools_combo_box.addItem("Sign forms")
        more_tools_combo_box.addItem("Compress file")
        self.addWidget(more_tools_combo_box)

    def close_edit_window(self):
        if self.edit_window:
            self.edit_window.close()
            self.edit_window = None
            self.active_edit = None

    def crop_triggered(self):
        if self.active_edit != "crop":
            self.close_edit_window()
            self.edit_window = CropEditWindow(self.pdf_tab)
            self.edit_window.resize(800, 550)
            self.edit_window.show()
            self.active_edit = "crop"
        else:
            self.close_edit_window()

    def rotate_triggered(self):
        if self.active_edit != "rotate":
            self.close_edit_window()
            self.edit_window = RotateEditWindow(self.pdf_tab)
            self.edit_window.resize(800, 550)
            self.edit_window.show()
            self.active_edit = "rotate"
        else:
            self.close_edit_window()

    def add_page_triggered(self):
        if self.active_edit != "add_page":
            self.close_edit_window()
            self.edit_window = AddPageEditWindow(self.pdf_tab)
            self.edit_window.resize(800, 550)
            self.edit_window.show()
            self.active_edit = "add_page"
        else:
            self.close_edit_window()

    def delete_page_triggered(self):
        if self.active_edit != "delete_page":
            self.close_edit_window()
            self.edit_window = DeletePageEditWindow(self.pdf_tab)
            self.edit_window.resize(800, 550)
            self.edit_window.show()
            self.active_edit = "delete_page"
        else:
            self.close_edit_window()

    def rearrange_triggered(self):
        if self.active_edit != "rearrange":
            self.close_edit_window()
            self.edit_window = RearrangeEditWindow(self.pdf_tab)
            self.edit_window.resize(800, 550)
            self.edit_window.show()
            self.active_edit = "rearrange"
        else:
            self.close_edit_window()

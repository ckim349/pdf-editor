from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QToolBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox
from PySide6.QtCore import QSize

class ToolBar(QToolBar):
    def __init__(self):
        super().__init__()

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
        self.addAction("&Rotate page")
        self.addAction("&Add page")
        self.addAction("&Delete page")
        self.addAction("&Rearrange pages")
        more_tools_combo_box = QComboBox()
        more_tools_combo_box.addItem("More tools")
        more_tools_combo_box.addItem("Combine pdfs")
        more_tools_combo_box.addItem("Sign forms")
        more_tools_combo_box.addItem("Compress file")
        self.addWidget(more_tools_combo_box)

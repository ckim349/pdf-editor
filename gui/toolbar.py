from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QToolBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import QSize

class ToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.setIconSize(QSize(20, 20))
        self.addAction("&Save")
        self.addAction("&Print")
        self.addAction("&Find")

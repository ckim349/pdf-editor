import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from widget import Widget

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Good Pdf Editor")

        menubar = self.menuBar()
        file = menubar.addMenu("&File")
        open_action = file.addAction("&Open")
        file.addSeparator()

        save_as_action = file.addAction("&Save as")
        save_as_action.triggered.connect(self.save_as)
        file.addSeparator()

        quit_action = file.addAction("&Quit")
        quit_action.triggered.connect(self.quit)


        edit = menubar.addMenu("&Edit")
        undo_action = edit.addAction("&Undo")
        redo_action = edit.addAction("&Redo")
        edit.addSeparator()
        cut_action = edit.addAction("&Cut")
        copy_action = edit.addAction("&Copy")
        paste_action = edit.addAction("&Paste")


        view = menubar.addMenu("&View")


        sign = menubar.addMenu("&Sign")


        window = menubar.addMenu("&Window")


        help = menubar.addMenu("&Help")


        toolbar = QToolBar("Tool Bar for Tools")
        toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(toolbar)

        toolbar.addAction("&Save")
        toolbar.addAction("&Print")
        toolbar.addAction("&Find")


    def quit(self):
        self.app.quit()

    def save_as(self):
        save_as_widget = Widget()
        save_as_widget.show()
        return save_as_widget

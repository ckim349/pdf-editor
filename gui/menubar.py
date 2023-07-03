from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QMenuBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QFileDialog
from PySide6 import QtCore
from save_widget import SaveWidget

class MenuBar(QMenuBar):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow

        file = self.addMenu("&File")
        open_action = file.addAction("&Open")
        # file_dialog = QFileDialog()
        # file_dialog.setNameFilter("PDF Files (*.pdf)")
        # file_dialog.setWindowTitle('Open folder...')
        # open_action.triggered.connect(self.open_file())

        file.addSeparator()

        save_as_action = file.addAction("&Save as")
        save_as_action.triggered.connect(self.save_as)
        file.addSeparator()

        quit_action = file.addAction("&Quit")
        quit_action.triggered.connect(self.mainwindow.quit)

        edit = self.addMenu("&Edit")
        undo_action = edit.addAction("&Undo")
        redo_action = edit.addAction("&Redo")
        edit.addSeparator()
        cut_action = edit.addAction("&Cut")
        copy_action = edit.addAction("&Copy")
        paste_action = edit.addAction("&Paste")

        view = self.addMenu("&View")

        sign = self.addMenu("&Sign")

        window = self.addMenu("&Window")

        help = self.addMenu("&Help")

        self.save_as_widget = None

    def save_as(self):
        if self.save_as_widget is None:
            self.save_as_widget = SaveWidget()
        self.save_as_widget.show()

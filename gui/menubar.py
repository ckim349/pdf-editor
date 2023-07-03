from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QTextEdit, QMenuBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QFileDialog, QMessageBox
from PySide6.QtCore import QUrl
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
        # open_action.triggered.connect(self.open_file)

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

        help = self.addMenu("&Help")
        about_action = help.addAction("&About")
        about_action.triggered.connect(self.about_triggered)

        self.save_as_widget = None

    def save_as(self):
        if self.save_as_widget is None:
            self.save_as_widget = SaveWidget()
        self.save_as_widget.show()

    def about_triggered(self):
        ret = QMessageBox.information(
            self,
            "About Chulshin's Goodey Pdf Editor",
            "Chulshin's Goodey Pdf Editor is a free to use pdf editor. Check out my github: https://github.com/ckim349",
            QMessageBox.Ok | QMessageBox.Cancel
        )
import sys
from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QTextEdit, QMenuBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QFileDialog, QMessageBox, QDialog
from PySide6.QtCore import QUrl, Slot, QStandardPaths
from PySide6.QtPdf import QPdfDocument

class MenuBar(QMenuBar):
    def __init__(self, main_window, pdf_tab):
        super().__init__()
        self.main_window = main_window
        self.pdf_tab = pdf_tab

        file = self.addMenu("&File")
        open_action = file.addAction("&Open")
        open_action.triggered.connect(self.pdf_tab.open_triggered)

        file.addSeparator()

        save_as_action = file.addAction("&Save as")
        save_as_action.triggered.connect(self.pdf_tab.save_triggered)
        file.addSeparator()

        quit_action = file.addAction("&Quit")
        quit_action.triggered.connect(self.main_window.quit)

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

    def about_triggered(self):
        ret = QMessageBox.information(
            self,
            "About Chulshin's Goodey Pdf Editor",
            "Chulshin's Goodey Pdf Editor is a free to use pdf editor. Check out my github: https://github.com/ckim349",
            QMessageBox.Ok | QMessageBox.Cancel
        )

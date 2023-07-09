import sys
from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QToolBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QDialog, QFileDialog
from PySide6.QtPdf import QPdfDocument, QPdfPageNavigator
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtPdf import QPdfPageNavigator
from PySide6.QtCore import QUrl, Slot, QStandardPaths
from scripts.pagehelper import save_as, output


class EditWindowPdf(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pdf_document = QPdfDocument(self)
        self.page_nav = QPdfPageNavigator()

        pdf_view = QPdfView(self)
        pdf_view.setDocument(self.pdf_document)
        pdf_view.setPageMode(QPdfView.PageMode.MultiPage)
        pdf_view.setZoomFactor(0.75)

        self.setLayout(QVBoxLayout())
        self.setCentralWidget(pdf_view)

    @Slot(QUrl)
    def open(self, doc_location):
        self.pdf_document.load(doc_location.toLocalFile())

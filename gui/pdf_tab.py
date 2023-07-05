import sys
from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QToolBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QDialog, QFileDialog
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtCore import QUrl, Slot, QStandardPaths
from toolbar import ToolBar

class PdfTab(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pdf_document = QPdfDocument(self)
        self.pdf_file_dialog = None

        toolbar = ToolBar()
        self.addToolBar(toolbar)

        pdf_view = QPdfView(self)
        pdf_view.setDocument(self.pdf_document)
        pdf_view.setPageMode(QPdfView.PageMode.MultiPage)

        self.setLayout(QVBoxLayout())
        self.setCentralWidget(pdf_view)

    @Slot(QUrl)
    def open(self, doc_location):
        if doc_location.isLocalFile():
            self.pdf_document.load(doc_location.toLocalFile())
            document_title = self.pdf_document.metaData(QPdfDocument.MetaDataField.Title)
            self.setWindowTitle(document_title if document_title else "PDF Viewer")
        else:
            message = f"{doc_location} is not a valid local file"
            print(message, file=sys.stderr)
            QMessageBox.critical(self, "Failed to open", message)

    @Slot()
    def open_triggered(self):
        if not self.pdf_file_dialog:
            directory = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
            self.pdf_file_dialog = QFileDialog(self, "Choose a PDF", directory)
            self.pdf_file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
            self.pdf_file_dialog.setMimeTypeFilters(["application/pdf"])
        if self.pdf_file_dialog.exec() == QDialog.Accepted:
            to_open = self.pdf_file_dialog.selectedUrls()[0]
            if to_open.isValid():
                self.open(to_open)

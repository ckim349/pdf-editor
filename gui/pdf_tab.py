import sys
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QMessageBox, QDialog, QFileDialog
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtCore import QUrl, Slot, QStandardPaths
from toolbar import ToolBar
from history import History
from pagehelper import save_as


class PdfTab(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.pdf_document = QPdfDocument(self)
        self.pdf_file_dialog = None
        self.pdf_file_dialog_save = None
        self.file_opened = False
        self.current_pdf = None
        self.reload_reference = None

        self.history = History(self)

        self.toolbar = ToolBar(self)
        self.addToolBar(self.toolbar)

        self.pdf_view = QPdfView(self)
        self.pdf_view.setDocument(self.pdf_document)
        self.pdf_view.setPageMode(QPdfView.PageMode.MultiPage)

        self.setLayout(QVBoxLayout())
        self.setCentralWidget(self.pdf_view)

    @Slot(QUrl)
    def open(self, doc_location):
        if doc_location.isLocalFile():
            self.reload_reference = doc_location
            self.pdf_document.load(doc_location.toLocalFile())
            self.main_window.tab_widget.insertTab(-1, self, doc_location.toString().split('/')[-1])
            self.main_window.set_tab(1)
            self.file_opened = True
            self.current_pdf = doc_location.toString()
        else:
            message = f"{doc_location} is not a valid local file"
            print(message, file=sys.stderr)
            QMessageBox.critical(self, "Failed to open", message)

    @Slot()
    def open_triggered(self):
        if not self.pdf_file_dialog:
            directory = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
            self.pdf_file_dialog = QFileDialog(self, "Open", directory)
            self.pdf_file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
            self.pdf_file_dialog.setMimeTypeFilters(["application/pdf"])
        if self.pdf_file_dialog.exec() == QDialog.Accepted:
            to_open = self.pdf_file_dialog.selectedUrls()[0]
            if to_open.isValid():
                self.open(to_open)

    @Slot()
    def save_triggered(self):
        if self.file_opened:
            if not self.pdf_file_dialog_save:
                directory = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
                self.pdf_file_dialog_save = QFileDialog(self, "Save as", directory)
                self.pdf_file_dialog_save.setAcceptMode(QFileDialog.AcceptSave)
                self.pdf_file_dialog_save.setMimeTypeFilters(["application/pdf"])
            if self.pdf_file_dialog_save.exec() == QDialog.Accepted:
                to_save = self.pdf_file_dialog_save.selectedUrls()[0]
                if to_save.isValid():
                    save_as(self.current_pdf[8:], '/'.join(to_save.toDisplayString()[8:].split('/')[:-1]) + '/' + to_save.fileName())
        else:
            message = "You can't save a file that's not open!"
            print(message)
            QMessageBox.critical(self, "Failed to open", message)

    def update_page(self):
        self.open(self.reload_reference)
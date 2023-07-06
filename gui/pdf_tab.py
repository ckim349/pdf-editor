import sys

from PySide6.QtPrintSupport import QPrinter
from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QToolBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QDialog, QFileDialog
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtCore import QUrl, Slot, QStandardPaths
from PySide6.QtGui import QPdfWriter, QPainter, QPageSize
from PySide6 import QtCore
from toolbar import ToolBar

class PdfTab(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        self.pdf_document = QPdfDocument(self)
        self.pdf_file_dialog = None
        self.pdf_file_dialog_save = None
        self.file_opened = False

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
            self.mainwindow.setTab(1)
            self.file_opened = True
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
    def save(self, file_name):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFileName(file_name)
        printer.setOutputFormat(QPrinter.PdfFormat)

        painter = QPainter(printer)
        self.render(painter)
        painter.end()

        # writer = QPdfWriter(file_name)
        # writer.setPageSize(QPageSize(self.centralWidget().size()))
        #
        # painter = QPainter(writer)
        # self.centralWidget().render(painter)
        #
        # painter.end()
        # writer.end()

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
                    self.save(to_save.fileName())
                    # print(to_save.fileName())
        else:
            message = "You can't save a file that's not open!"
            print(message)
            QMessageBox.critical(self, "Failed to open", message)
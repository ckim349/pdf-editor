import sys
from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QToolBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QDialog, QFileDialog
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtCore import QUrl, Slot, QStandardPaths
from PySide6 import QtCore
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from toolbar import ToolBar
from menubar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Chulshin's Goodey Pdf Editor")
        self.pdf_document = QPdfDocument(self)
        self.pdf_file_dialog = None

        # Menubar
        menubar = MenuBar(self)
        self.setMenuBar(menubar)

        # Tabs
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        tab_widget = QTabWidget(central_widget)
        home_tab = QWidget()
        pdf_tab = QMainWindow()

        tab_widget.addTab(home_tab, "Home")
        tab_widget.addTab(pdf_tab, "Pdf Editor")

        # Toolbar
        toolbar = ToolBar()
        pdf_tab.addToolBar(toolbar)

        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(tab_widget)

        # PDF Document
        pdf_view = QPdfView(pdf_tab)
        pdf_view.setDocument(self.pdf_document)
        pdf_view.setPageMode(QPdfView.PageMode.MultiPage)

        pdf_tab.setLayout(QVBoxLayout())
        pdf_tab.setCentralWidget(pdf_view)

        self.setLayout(main_layout)

    def quit(self):
        self.app.quit()


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
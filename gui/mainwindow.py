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
from pdf_tab import PdfTab

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Chulshin's Goodey Pdf Editor")
        pdf_tab = PdfTab()

        menubar = MenuBar(self, pdf_tab)
        self.setMenuBar(menubar)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        tab_widget = QTabWidget(central_widget)
        home_tab = QWidget()

        tab_widget.addTab(home_tab, "Home")
        tab_widget.addTab(pdf_tab, "Pdf Editor")

        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(tab_widget)

        self.setLayout(main_layout)

    def quit(self):
        self.app.quit()

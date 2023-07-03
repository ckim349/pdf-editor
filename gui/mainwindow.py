import sys
from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QToolBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6 import QtCore
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView
from toolbar import ToolBar
from menubar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Chulshin's Goodey Pdf Editor")

        # Menubar
        menubar = MenuBar(self)
        self.setMenuBar(menubar)

        # Tabs
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        tab_widget = QTabWidget(central_widget)
        home_tab = QWidget()
        pdf_tab = QMainWindow()

        pdf_tab_layout = QVBoxLayout()
        pdf_tab.setLayout(pdf_tab_layout)

        tab_widget.addTab(home_tab, "Home")
        tab_widget.addTab(pdf_tab, "Pdf Editor")

        # Toolbar
        toolbar = ToolBar()
        pdf_tab.addToolBar(toolbar)

        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(tab_widget)

        self.setLayout(main_layout)

    def quit(self):
        self.app.quit()

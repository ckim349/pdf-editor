from PySide6.QtWidgets import QTabWidget, QMainWindow, QWidget, QVBoxLayout, QPushButton, QToolButton, QSizePolicy
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt
from menubar import MenuBar
from pdf_tab import PdfTab

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Chulshin's Goodey Pdf Editor")
        pdf_tab = PdfTab(self)

        menubar = MenuBar(self, pdf_tab)
        self.setMenuBar(menubar)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.tab_widget = QTabWidget(central_widget)
        self.tab_widget.tabBar().setExpanding(True)
        home_tab = QWidget()
        home_layout = QVBoxLayout()

        open_button = QToolButton()
        open_button.setIcon(QIcon("../icon/folder_open.png"))
        open_button.setIconSize(QSize(100, 100))
        open_button.clicked.connect(pdf_tab.open_triggered)

        open_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        open_button.setStyleSheet("QPushButton { text-align: center; }")
        home_layout.addStretch(1)
        home_layout.addWidget(open_button, alignment=Qt.AlignCenter)
        home_layout.addStretch(1)
        home_tab.setLayout(home_layout)


        self.tab_widget.addTab(home_tab, "Home")

        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(self.tab_widget)

        self.setLayout(main_layout)

    def quit(self):
        self.app.quit()

    def set_tab(self, index):
        self.tab_widget.setCurrentIndex(index)

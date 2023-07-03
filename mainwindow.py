import sys
from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow, QToolBar, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from save_widget import SaveWidget

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Good Pdf Editor")

        menubar = self.menuBar()
        file = menubar.addMenu("&File")
        open_action = file.addAction("&Open")
        file.addSeparator()

        save_as_action = file.addAction("&Save as")
        save_as_action.triggered.connect(self.save_as)
        file.addSeparator()

        quit_action = file.addAction("&Quit")
        quit_action.triggered.connect(self.quit)


        edit = menubar.addMenu("&Edit")
        undo_action = edit.addAction("&Undo")
        redo_action = edit.addAction("&Redo")
        edit.addSeparator()
        cut_action = edit.addAction("&Cut")
        copy_action = edit.addAction("&Copy")
        paste_action = edit.addAction("&Paste")


        view = menubar.addMenu("&View")


        sign = menubar.addMenu("&Sign")


        window = menubar.addMenu("&Window")


        help = menubar.addMenu("&Help")


        toolbar = QToolBar("Tool Bar for Tools")
        toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(toolbar)

        toolbar.addAction("&Save")
        toolbar.addAction("&Print")
        toolbar.addAction("&Find")

        self.save_as_widget = None

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        tab_widget = QTabWidget(central_widget)
        home_tab = QWidget()
        pdf_tab = QWidget()

        tab_widget.addTab(home_tab, "Home")
        tab_widget.addTab(pdf_tab, "Pdf Editor")

        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(tab_widget)

        self.setLayout(main_layout)

    def quit(self):
        self.app.quit()


    def save_as(self):
        if self.save_as_widget is None:  # Only create the widget if it doesn't exist
            self.save_as_widget = SaveWidget()
        self.save_as_widget.show()
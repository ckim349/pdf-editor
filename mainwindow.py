from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Good Pdf Editor")

        menubar = self.menuBar()
        file = menubar.addMenu("File")
        quit_action = file.addAction("Quit")
        quit_action.triggered.connect(self.quit)

    def quit(self):
        self.app.quit()
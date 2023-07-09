import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from main_window import MainWindow


app = QApplication(sys.argv)

window = MainWindow(app)
window.showMaximized()
app.exec()

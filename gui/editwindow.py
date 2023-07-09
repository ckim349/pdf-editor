from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGridLayout

class BaseEditWindow(QWidget):
    def __init__(self):
        super().__init__()

        grid_layout = QGridLayout()
        grid_layout.addWidget(QPushButton("Testing"),0,0,2,2)
        self.setLayout(grid_layout)

class CropEditWindow(BaseEditWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop")

class RotateEditWindow(BaseEditWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rotate")

class AddPageEditWindow(BaseEditWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Page")

class DeletePageEditWindow(BaseEditWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Page")

class RearrangePageEditWindow(BaseEditWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rearrange Pages")
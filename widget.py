from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Save as")

        filename_label = QLabel("Filename: ")
        filename_line_edit = QLineEdit()

        save_as_label = QLabel("Save as: ")
        save_as_line_edit = QLineEdit()

        filename_layout = QHBoxLayout()
        filename_layout.addWidget(filename_label)
        filename_layout.addWidget(filename_line_edit)

        save_as_layout = QHBoxLayout()
        save_as_layout.addWidget(save_as_label)
        save_as_layout.addWidget(save_as_line_edit)

        main_layout = QVBoxLayout()
        main_layout.addLayout(filename_layout)
        main_layout.addLayout(save_as_layout)






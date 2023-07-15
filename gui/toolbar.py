import os
from PySide6.QtWidgets import QToolBar, QMessageBox, QComboBox, QDialog, QFileDialog
from PySide6.QtCore import QSize, QStandardPaths
from edit_window import RotateEditWindow, CropEditWindow, AddPageEditWindow, DeletePageEditWindow, RearrangeEditWindow
from pagehelper import merge_two_pdfs, compress


class ToolBar(QToolBar):
    def __init__(self, pdf_tab):
        super().__init__()
        self.pdf_tab = pdf_tab
        self.edit_window = None
        self.active_edit = None
        self.merge_open = False
        self.file_dialog = None

        self.setIconSize(QSize(20, 20))

        zoom_out_action = self.addAction("&Zoom out")
        zoom_out_action.triggered.connect(self.zoom_out_triggered)
        zoom_in_action = self.addAction("&Zoom in")
        zoom_in_action.triggered.connect(self.zoom_in_triggered)
        self.addSeparator()

        crop_action = self.addAction("&Crop")
        crop_action.triggered.connect(self.crop_triggered)

        rotate_action = self.addAction("&Rotate page")
        rotate_action.triggered.connect(self.rotate_triggered)

        add_page_action = self.addAction("&Add page")
        add_page_action.triggered.connect(self.add_page_triggered)

        delete_page_action = self.addAction("&Delete page")
        delete_page_action.triggered.connect(self.delete_page_triggered)

        rearrange_action = self.addAction("&Rearrange pages")
        rearrange_action.triggered.connect(self.rearrange_triggered)
        self.addSeparator()

        merge_action = self.addAction("&Merge pdfs")
        merge_action.triggered.connect(self.merge_triggered)

        compress_action = self.addAction("&Compress")
        compress_action.triggered.connect(self.compress_triggered)

    def close_edit_window(self):
        if self.edit_window:
            self.edit_window.close()
            self.edit_window = None
            self.active_edit = None

    def crop_triggered(self):
        if self.active_edit != "crop":
            self.close_edit_window()
            self.edit_window = CropEditWindow(self.pdf_tab)
            self.edit_window.resize(800, 550)
            self.edit_window.show()
            self.active_edit = "crop"
        else:
            self.close_edit_window()

    def rotate_triggered(self):
        if self.active_edit != "rotate":
            self.close_edit_window()
            self.edit_window = RotateEditWindow(self.pdf_tab)
            self.edit_window.resize(800, 550)
            self.edit_window.show()
            self.active_edit = "rotate"
        else:
            self.close_edit_window()

    def add_page_triggered(self):
        if self.active_edit != "add_page":
            self.close_edit_window()
            self.edit_window = AddPageEditWindow(self.pdf_tab)
            self.edit_window.resize(800, 550)
            self.edit_window.show()
            self.active_edit = "add_page"
        else:
            self.close_edit_window()

    def delete_page_triggered(self):
        if self.active_edit != "delete_page":
            self.close_edit_window()
            self.edit_window = DeletePageEditWindow(self.pdf_tab)
            self.edit_window.resize(800, 550)
            self.edit_window.show()
            self.active_edit = "delete_page"
        else:
            self.close_edit_window()

    def rearrange_triggered(self):
        if self.active_edit != "rearrange":
            self.close_edit_window()
            self.edit_window = RearrangeEditWindow(self.pdf_tab)
            self.edit_window.resize(800, 550)
            self.edit_window.show()
            self.active_edit = "rearrange"
        else:
            self.close_edit_window()

    def zoom_out_triggered(self):
        if self.pdf_tab.pdf_view.zoomFactor() > 0.25:
            self.pdf_tab.pdf_view.setZoomFactor(self.pdf_tab.pdf_view.zoomFactor() - 0.25)

    def zoom_in_triggered(self):
        self.pdf_tab.pdf_view.setZoomFactor(self.pdf_tab.pdf_view.zoomFactor() + 0.25)

    def merge_triggered(self):
        if not self.merge_open:
            directory = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
            self.file_dialog = QFileDialog(self, "Open", directory)
            self.file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
            self.file_dialog.setMimeTypeFilters(["application/pdf"])
        if self.file_dialog.exec() == QDialog.Accepted:
            to_open = self.file_dialog.selectedUrls()[0]
            if to_open.isValid():
                merge_two_pdfs(self.pdf_tab.current_pdf[8:], to_open.toString()[8:])
        ret = QMessageBox.information(
            self.pdf_tab,
            "Merge information",
            "Merge was successful!",
            QMessageBox.Ok | QMessageBox.Cancel
        )

    def compress_triggered(self):
        path = self.pdf_tab.current_pdf[8:]
        file_size = os.path.getsize(path) / (1024 * 1024)
        compress(path)
        new_size = os.path.getsize(f"{os.path.split(path)[0]}/compressed-{path.split('/')[-1][:-4]}.pdf") / (1024 * 1024)
        if new_size < file_size:
            ret = QMessageBox.information(
                self.pdf_tab,
                "Compress information",
                f"Compress was successful! You have compressed {path.split('/')[-1][:-4]}.pdf by {file_size - new_size:.4f}mb!"
                f" Check out your new file compressed-{path.split('/')[-1][:-4]}.pdf.",
                QMessageBox.Ok | QMessageBox.Cancel
            )
        elif new_size > file_size:
            ret = QMessageBox.information(
                self.pdf_tab,
                "Compress information",
                f"Uh oh. Compress was not successful... {path.split('/')[-1][:-4]}.pdf has increased in size by {new_size - file_size:.4f}mb!"
                f" Check out your new file compressed-{path.split('/')[-1][:-4]}.pdf.",
                QMessageBox.Ok | QMessageBox.Cancel
            )
        else:
            ret = QMessageBox.information(
                self.pdf_tab,
                "Compress information",
                f"Eyy, sometimes things just have to stay the same. Compression unsuccessful"
                f" Check out your new file compressed-{path.split('/')[-1][:-4]}.pdf.",
                QMessageBox.Ok | QMessageBox.Cancel
            )
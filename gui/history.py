from scripts.pagehelper import add_page, rotate, delete_page, crop, rearrange, get_coords, save_page


class History():
    def __init__(self, pdf_tab):
        self.undo_stack = []
        self.redo_stack = []
        self.pdf_tab = pdf_tab

    def undo(self):
        if self.undo_stack:
            current = self.undo_stack.pop()
            path = self.pdf_tab.current_pdf[8:]
            page_number = current[1]

            if current[0] == "rotate":
                rotate(path, page_number)
                rotate(path, page_number)
                rotate(path, page_number)
                self.redo_stack.append(("rotate", page_number))
            elif current[0] == "add_page":
                page = save_page(path, page_number)
                self.redo_stack.append(("delete_page", page_number, page))
                delete_page(path, page_number)
            elif current[0] == "delete_page":
                add_page(path, page_number, current[2])
                self.redo_stack.append(("add_page", page_number))
            elif current[0] == "crop":
                (l_l_x, l_l_y, u_r_x, u_r_y) = get_coords(path, page_number)
                self.redo_stack.append(
                    ("crop", page_number, l_l_x, l_l_y, u_r_x, u_r_y)
                )
                crop(path,page_number, current[2], current[3], current[4], current[5])
            elif current[0] == "rearrange":
                rearrange(path, page_number, current[2])
                self.redo_stack.append(("rearrange", page_number, current[2]))

    def redo(self):
        if self.redo_stack:
            current = self.redo_stack.pop()
            path = self.pdf_tab.current_pdf[8:]
            page_number = current[1]

            if current[0] == "rotate":
                rotate(path, page_number)
                self.undo_stack.append(("rotate", page_number))
            elif current[0] == "add_page":
                delete_page(path, page_number)
                self.undo_stack.append(("add_page", page_number))
            elif current[0] == "delete_page":
                add_page(path, page_number, current[2])
                self.undo_stack.append(("delete_page", page_number, current[2]))
            elif current[0] == "crop":
                (l_l_x, l_l_y, u_r_x, u_r_y) = get_coords(path, page_number)
                self.undo_stack.append(
                    ("crop", page_number, l_l_x, l_l_y, u_r_x, u_r_y)
                )
                crop(path, page_number, current[2], current[3], current[4], current[5])
            elif current[0] == "rearrange":
                rearrange(path, page_number, current[2])
                self.undo_stack.append(("rearrange", page_number, current[2]))

from scripts.pagehelper import add_page, rotate, delete_page, crop, rearrange


class History():
    def __init__(self, pdf_tab):
        self.undo_stack = []
        self.redo_stack = []
        self.pdf_tab = pdf_tab

    def undo(self):
        if self.undo_stack:
            current = self.undo_stack.pop()
            print(current)
            path = self.pdf_tab.current_pdf[8:]

            if current[0] == "rotate":
                print("we in")
                rotate(path, current[1])
                rotate(path, current[1])
                rotate(path, current[1])
            elif current[0] == "add_page":
                delete_page(path, current[1])
            elif current[0] == "delete_page":
                pass
            elif current[0] == "crop":
                pass
            elif current[0] == "rearrange":
                rearrange(path, current[2], current[1])


    def redo(self):
        pass

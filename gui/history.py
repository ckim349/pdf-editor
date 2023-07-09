
class History():
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def undo(self):
        if self.undo_stack:
            current = self.undo_stack.pop()

    def redo(self):
        pass

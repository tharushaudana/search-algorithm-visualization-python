class Node:
    def __init__(self, cell, parent):
        self.cell = cell
        self.parent = parent

class AstarNode(Node):
    def __init__(self, cell, parent):
        super().__init__(cell, parent)
        self.h = -1 # heuristic value
        self.g = 0 # current steps

    def gh(self):
        return self.g + self.h
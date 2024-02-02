from graphics import *
from .cell import Cell

class Maze:
    def __init__(self, maze):
        self.maze = maze

        self.cells = []
        self.start_cell = None
        self.end_cell = None

        self.width = None
        self.height = None
        self.win = GraphWin(title="Maze Window", width=800, height=800)

    def drawMaze(self):
        for row in self.cells:
            for cell in row:
                cell.draw(self.win) 

    def init(self):
        f = open(self.maze, "r")

        y = 0

        for line in f.readlines():
            x = 0

            self.cells.append([])

            for c in line:
                if c == "\n": continue

                cell = Cell((x, y))

                if c == " ":
                    cell.type = Cell.Normal
                elif c == "#":
                    cell.type = Cell.Wall
                elif c == "A":
                    cell.type = Cell.Start
                    self.start_cell = cell
                elif c == "B":
                    cell.type = Cell.End
                    self.end_cell = cell

                self.cells[-1].append(cell)
                x += 1

            y += 1

        self.width = x
        self.height = y

        f.close()
        self.drawMaze()

    def neighbours(self, cell):
        n = []

        #left
        if cell.x > 0:
            n.append(self.cells[cell.y][cell.x - 1])
        #right
        if cell.x < self.width - 1:
            n.append(self.cells[cell.y][cell.x + 1])
        #top
        if cell.y > 0:
            n.append(self.cells[cell.y - 1][cell.x])
        #bottom
        if cell.y < self.height - 1:
            n.append(self.cells[cell.y + 1][cell.x])

        for i in n:
            if i.type != Cell.Wall:
                yield i

    def drawPathFromEnd(self, node, col):
        while True:
            node = node.parent
            node.cell.drawWithCustomColor(self.win, col)
            if node.parent == None: break

    def solve_by(self, algo):
        algo.solve(self)
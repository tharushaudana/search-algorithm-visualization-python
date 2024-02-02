from time import sleep
from ..frontier import StackFrontier
from ..node import Node

class BFS:
    def __init__(self):
        self.frontier = StackFrontier()
        self.delay = None

    def solve(self, maze):
        self.frontier.add(Node(maze.start_cell, None))

        while True:
            if self.frontier.is_empty():
                raise Exception("Frontier is Empty! Unable to solve.")
            
            node = self.frontier.remove()

            # check if node is the End
            if node.cell.pos == maze.end_cell.pos:
                maze.drawPathFromEnd(node, 'green')
                break

            # add neighbours into Frontier
            for cell in maze.neighbours(node.cell):
                self.frontier.add(Node(cell=cell, parent=node))

            # draw it in yellow color
            node.cell.drawWithCustomColor(maze.win, 'yellow')

            if self.delay != None:
                sleep(self.delay)
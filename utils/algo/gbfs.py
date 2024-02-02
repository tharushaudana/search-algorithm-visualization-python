from time import sleep
from ..frontier import QueueFrontier
from ..node import Node

class GBFS:
    def __init__(self):
        self.frontier = QueueFrontier()
        self.delay = None

    # calculate the Heuristic value
    def calc_h(self, cell, end_cell):
        return abs(cell.x - end_cell.x) + abs(cell.y - end_cell.y)

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

            neighbours = list(maze.neighbours(node.cell))

            ### when the removed node is not a 'Decision Point'
            if len(neighbours) == 1:
                self.frontier.add(Node(cell=neighbours[0], parent=node))
            ### when the removed node is a 'Decision Point'
            else:
                # calculate the heuristics values of neighbours, who not explored yet
                heuristics = {} 
                for cell in neighbours:
                    if self.frontier.is_explored(cell): continue
                    n = Node(cell=cell, parent=node)
                    h = self.calc_h(cell, maze.end_cell)
                    if h not in heuristics: heuristics[h] = list()
                    heuristics[h].append(n)

                # sorting the heuristics values to DESC order
                values = list(heuristics.keys())
                values.sort(reverse=True)

                # then add them in to Frontier
                for _ in [heuristics[_] for _ in values]:
                    for n in _:
                        self.frontier.add(n)

            # draw it in yellow color
            node.cell.drawWithCustomColor(maze.win, 'yellow')

            if self.delay != None:
                sleep(self.delay)
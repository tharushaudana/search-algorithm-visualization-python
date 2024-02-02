from time import sleep
from ..frontier import QueueFrontier
from ..node import AstarNode as Node

class ASTAR:
    def __init__(self):
        self.frontier = QueueFrontier()
        self.delay = None

    # calculate the Heuristic value
    def calc_h(self, cell, end_cell):
        return abs(cell.x - end_cell.x) + abs(cell.y - end_cell.y)
    
    # check if the optimal path
    def is_not_optimal_path(self, next_node):
        if len(self.frontier.frontier) == 0: return False
        return self.frontier.frontier[-1].gh() < next_node.gh()

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

            # calculate the 'heuristics values' and add 'step cost' of neighbours, who not explored yet
            heuristics = {} 
            for cell in neighbours:
                if self.frontier.is_explored(cell): continue

                n = Node(cell=cell, parent=node)
                n.g = node.g + 1
                n.h = self.calc_h(cell, maze.end_cell)
                
                # add the neighbour to front, when is not an optimal path
                if self.is_not_optimal_path(n):
                    self.frontier.add_front(n)
                    #n.cell.drawText(maze.win, "%d+%d" % (n.h, n.g))
                    continue

                if n.gh() not in heuristics: heuristics[n.gh()] = list()
                heuristics[n.gh()].append(n)

            if len(heuristics) > 0:
                # sorting the heuristics values to DESC order
                values = list(heuristics.keys())
                values.sort(reverse=True)

                # then add them in to Frontier
                for _ in [heuristics[_] for _ in values]:
                    for n in _:
                        self.frontier.add(n)

            # draw it in yellow color
            node.cell.drawWithCustomColor(maze.win, 'yellow')
            #node.cell.drawText(maze.win, "%d+%d" % (node.h, node.g))

            if self.delay != None:
                sleep(self.delay)
class Frontier:
    def __init__(self):
        self.frontier = []
        self.explored = set()

    def is_explored(self, cell):
        return cell.pos in self.explored

    def is_empty(self):
        return len(self.frontier) == 0
    
class StackFrontier(Frontier):
    def __init__(self):
        super().__init__()

    def add(self, node):
        if node.cell.pos in self.explored: return
        print(len(self.frontier))
        self.frontier.append(node)

    def remove(self):
        node = self.frontier[0]
        self.explored.add(node.cell.pos)
        self.frontier.pop(0)
        return node

class QueueFrontier(Frontier):
    def __init__(self):
        super().__init__()

    def add(self, node):
        if node.cell.pos in self.explored: return
        self.frontier.append(node)

    def remove(self):
        node = self.frontier[-1]
        self.explored.add(node.cell.pos)
        self.frontier.pop(-1)
        return node
    
    # this method is only using for A* algorithm
    def add_front(self, node):
        if node.cell.pos in self.explored: return
        self.frontier.insert(0, node)
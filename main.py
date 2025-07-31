from utils.maze import Maze
from utils.algo import DFS, BFS, GBFS, ASTAR

maze = Maze("maze2.txt")

# algo = DFS()
# algo = BFS()
# algo = GBFS()
algo = ASTAR()

algo.delay = 0.01

maze.init()

maze.solve_by(algo)

while True:
    pass

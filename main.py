from utils.maze import Maze
from utils.algo import DFS, BFS, GBFS, ASTAR

maze = Maze("maze5.txt")

algo = ASTAR()
algo.delay = 0.1

maze.init()

maze.solve_by(algo)

while True:
    pass

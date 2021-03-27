from h1 import heuristic_h1
from h2 import heuristic_h2
from h3 import heuristic_h3

def heuristic_h5(node_board):
    return max(heuristic_h1(node_board), heuristic_h2(node_board), heuristic_h3(node_board))
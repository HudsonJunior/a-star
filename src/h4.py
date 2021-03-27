from h1 import heuristic_h1
from h2 import heuristic_h2
from h3 import heuristic_h3

def heuristic_h4(node_board):
    p1 = 0.3
    p2 = 0.3
    p3 = 0.4

    return (p1 * heuristic_h1(node_board)) + (p2 * heuristic_h2(node_board)) + (p3 * heuristic_h3(node_board))
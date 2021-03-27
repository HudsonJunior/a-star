from heapq import heappop
import copy
from NodeBoard import node_board

def get_node_less_total_cost(heap, A):
    while True:
        element = heappop(heap)
        if element[1] in A:
            return A.get(element[1])

def change_part(node, part):
    new_node = copy.deepcopy(node.board_state)

    new_node[node.white_space[0]][node.white_space[1]] = node.board_state[part[0]][part[1]]
    new_node[part[0]][part[1]] = node.board_state[node.white_space[0]][node.white_space[1]]

    return node_board(new_node, part, node)

def generate_successors(node):
    white_space = node.white_space
    children = []
    ## move to the left
    if white_space[0] - 1 >= 0:
        child = change_part(node, (white_space[0] - 1, white_space[1]))
        child.g_cost = node.g_cost + 1
        child.h_cost = 0
        children.append(child)

    ## move to the up
    if white_space[1] - 1 >= 0:
        child = change_part(node, (white_space[0], white_space[1] - 1))
        child.g_cost = node.g_cost + 1
        child.h_cost = 0
        children.append(child)

    ## move to the right
    if white_space[0] + 1 < 4:
        child = change_part(node, (white_space[0] + 1, white_space[1]))
        child.g_cost = node.g_cost + 1
        child.h_cost = 0
        children.append(child)

    ## move to the down
    if white_space[1] + 1 < 4:
        child = change_part(node, (white_space[0], white_space[1] + 1))
        child.g_cost = node.g_cost + 1
        child.h_cost = 0
        children.append(child)

    return children

def get_white_sace(board):
    for i in range(4):
        for j in range(4):
            if (int(board[i][j]) == 0): return (i,j)

def get_final_path(current_node, initial_board):
    path = []
    while current_node is not None:
        path.append(current_node.board_state)
        current_node = current_node.parent_node

    return path[::-1]
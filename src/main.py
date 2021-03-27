from NodeBoard import node_board
import copy
from heapq import heappush, heappop, heapify
from util import *
from h1 import heuristic_h1
from h2 import heuristic_h2
from h3 import heuristic_h3
from h4 import heuristic_h4
from h5 import heuristic_h5

expected_values = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 0]
final_board = [['1', '5', '9', '13'], ['2', '6', '10', '14'], ['3', '7', '11', '15'], ['4', '8', '12', '0']]

def algorithm_astar(initial_board):
    global final_board
    global expected_values

    ## criando estruturas A e F como dicionários para conseguir referenciar melhor
    A = {}
    F = {}

    heap_management = []

    # criando uma estrutura heap que servirá para realizar operações otimizadas no A e F
    heapify(heap_management)

    # inicia a lista de nós abertos
    initial_white_space = get_white_sace(initial_board)
    initial_node = node_board(initial_board, initial_white_space, None)

    A[str(initial_board)] = initial_node
    heappush(heap_management, (A[str(initial_board)].g_cost + A[str(initial_board)].h_cost, str(initial_board)))

    current_node = initial_node
    while A:
        ## recuperar o nó com o menor custo total
        current_node = get_node_less_total_cost(heap_management, A)

        ## Achou o caminho final, deve construir esse caminho
        if current_node.board_state == final_board:
           return get_final_path(current_node, initial_board)

        A.pop(str(current_node.board_state))
        F[str(current_node.board_state)] = current_node

        successors_nodes = generate_successors(current_node)
        
        for successor_node in successors_nodes:
            successor_node_converted = str(successor_node.board_state)

            if successor_node_converted in F: pass

            if successor_node_converted not in A and successor_node_converted not in F:
                A[successor_node_converted] = successor_node
                A[successor_node_converted].h_cost = heuristic_h3(successor_node, final_board)
                heappush(heap_management, (A[successor_node_converted].g_cost + A[successor_node_converted].h_cost, successor_node_converted))

            if successor_node_converted in A and A[successor_node_converted].g_cost > successor_node.g_cost:
                A.pop(successor_node_converted)

    return None
                
def main():
    entry = input().split(" ")

    # criar base do tabuleiro (4x4) com valores iniciais 0
    board = [[0 for i in range(4)] for i in range(4)]

    pos = 1

    # atribuir os valores de entrada para cada posição do tabuleiro
    for i in range(4):
        for j in range(4):
            board[i][j] = entry[pos]
            pos = pos + 1

    print(len(algorithm_astar(board)) - 1)

main()
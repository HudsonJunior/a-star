from NodeBoard import node_board
import copy
import heapq as hp
expected_values = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 0]
final_board = [['1', '5', '9', '13'], ['2', '6', '10', '14'], ['3', '7', '11', '15'], ['4', '8', '12', '0']]

A = set() # {}
F = set() # {}
g = []

## Escolha de utilizar a estrutura set() em python para representar os conjuntos A e F
## Sets são mais otimizados que listas para busca, com tempo constante O(1)
## A inserção nos sets varia de O(1) até O(n) no pior caso (utilizam de tecnicas hash para armazenar o valor)

## número de peças fora de lugar na config inicial
def heuristic_h1(node_board):
    global expected_values

    board = node_board.board_state
    i = -1
    count = 0

    for column in board:
        for pos in column:
            i = i + 1
            pos = int(pos)

            count = count + 1 if pos != 0 and pos != expected_values[i] else count + 0 

    return count

def get_node_less_total_cost(heap, A):
    while True:
        element = hp.heappop(heap)
        if element[0] in A:
            return A.get(element[0])

def change_part(node, part):
    new_node = copy.deepcopy(node.board_state)

    new_node[node.white_space[0]][node.white_space[1]] = node.board_state[part[0]][part[1]]
    new_node[part[0]][part[1]] = node.board_state[node.white_space[0]][node.white_space[1]]

    return node_board(new_node, part, node)

def generate_successors(node):
    white_space = node.white_space
    print('white white', white_space)
    children = []
    ## move to the left
    if white_space[0] - 1 >= 0:
        child = change_part(node, (white_space[0] - 1, white_space[1]))
        child.g_cost = node.g_cost + 1
        child.h_cost = 0
        child.parent_node = node
        children.append(child)

    ## move to the up
    if white_space[1] - 1 >= 0:
        child = change_part(node, (white_space[0], white_space[1] - 1))
        child.g_cost = node.g_cost + 1
        child.h_cost = 0
        child.parent_node = node
        children.append(child)

    ## move to the right
    if white_space[0] + 1 < 4:
        child = change_part(node, (white_space[0] + 1, white_space[1]))
        child.g_cost = node.g_cost + 1
        child.h_cost = 0
        child.parent_node = node
        children.append(child)

    ## move to the down
    if white_space[1] + 1 < 4:
        child = change_part(node, (white_space[0], white_space[1] + 1))
        child.g_cost = node.g_cost + 1
        child.h_cost = 0
        child.parent_node = node
        children.append(child)

    print(children)
    return children

def get_white_sace(board):
    for i in range(4):
        for j in range(4):
            if (int(board[i][j]) == 0): return (i,j)

def algorithm_astar(initial_board):
    global final_board

    ## criando estruturas A e F como dicionários para conseguir referenciar melhor
    A = {}
    F = {}

    heap_management = []

    # criando uma estrutura heap que servirá para realizar operações otimizadas no A e F
    hp.heapify(heap_management)

    # inicia a lista de nós abertos
    initial_white_space = get_white_sace(initial_board)
    initial_node = node_board(initial_board, initial_white_space, None)

    A[str(initial_board)] = initial_node
    hp.heappush(heap_management, (str(initial_board), A[str(initial_board)].g_cost + A[str(initial_board)].h_cost))

    current_node = initial_node
    
    while A:
        ## recuperar o nó com o menor custo total
        current_node = get_node_less_total_cost(heap_management, A)

        ## Achou o caminho final, deve construir esse caminho
        if current_node.board_state == final_board:
            path = []
            while current_node.board_state != initial_board:
                path.append(current_node.board_state)
                current_node = current_node.parent_node

            return path[::-1]

        A.pop(str(current_node.board_state))
        F[str(current_node.board_state)] = current_node

        successors_nodes = generate_successors(current_node)

        print('A', A)
        print('F',F)
        for successor_node in successors_nodes:
            print("sucessor", successor_node.board_state)
            successor_node_converted = str(successor_node.board_state)

            if successor_node_converted in F: continue

            if successor_node_converted not in A and successor_node_converted not in F:
                print('123')
                A[successor_node_converted] = successor_node
                A[successor_node_converted].h_cost = heuristic_h1(successor_node)
                hp.heappush(heap_management, (successor_node_converted, A[successor_node_converted].g_cost + A[successor_node_converted].h_cost))

            if successor_node_converted in A and A[successor_node_converted].g_cost > successor_node.g_cost:
                print('456')
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

    node = node_board(board, (0,0), None)
    out_parts = heuristic_h1(node)

    print('heuristic 1', out_parts)

    print('a estrela', algorithm_astar(board))

main()





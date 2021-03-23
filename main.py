from NodeBoard import node_board

expected_values = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 0]
adjacent_squares = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]

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

def get_node_less_total_cost(A):
    node = min(A, key=lambda node: node.g_cost + node.h_cost)
    return node

def generate_sucessor(parent_node, board):
    x, y = parent_node.position
    children = [board[adj[0]][adj[1]] for adj in [(x-1, y, (x, y-1), (x, y +1), (x + 1, y))]]
def algorithm_astar(board, start_node, end_node):
    global adjacent_squares

    A = set()
    F = set()

    # inicia a lista de nós abertos
    A.add(start_node)
    
    while len(A):
        ## recuperar o nó com o menor custo total
        current_node = get_node_less_total_cost(A)

        # remover da lista de nós abertos
        A.remove(current_node)

        # colocar ele na lista de nós fechados
        F.add(current_node)

        ## Achou o caminho final, deve construir esse caminho
        if current_node == end_node:
            path = []

            while current_node != start_node:
                path.append((current_node.board_state, current_node.position))
                current_node = current_node.parent_node

            return path[::-1]

        for possible_position in adjacent_squares:
            new_position = (current_node.)


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

    node = node_board(board, 0, 0, None)

    out_parts = heuristic_h1(node)

    print(out_parts)

main()





def heuristic_h3(node_board, final_board):
    board = node_board.board_state
    total_sum = 0

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0 and board[i][j] != final_board[i][j]:
                total_sum = total_sum + manhattan_distance(board[i][j], i ,j)

    return total_sum

def manhattan_distance(part, i ,j):
    ## definindo uma lista de tuplas (pq é imutável) das coordenadas que cada posição do vetor 1, 2, 3... estão supostas a estar
    correct_positions = [(3,3), (0,0), (1,0), (2,0), (3,0), (0,1), (1,1), (2,1), (3,1), (0,2), (1,2), (2,2), (3,2), (0,3), (1,3), (2,3)]

    return ((abs(i - correct_positions[int(part)][0])) + (abs(j - correct_positions[int(part)][1])))
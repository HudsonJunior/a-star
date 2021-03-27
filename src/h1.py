## número de peças fora de lugar na config inicial

def heuristic_h1(node_board, expected_values):
    board = node_board.board_state
    i = -1
    count = 0

    for column in board:
        for pos in column:
            i = i + 1
            pos = int(pos)

            count = count + 1 if pos != 0 and pos != expected_values[i] else count + 0 

    return count
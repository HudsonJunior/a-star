def heuristic_h2(node_board):
    entire_list = [int(positon) for sublist in node_board.board_state for positon in sublist]

    count = 0

    for element in range(len(entire_list)):
        if(element != 0 and entire_list[element - 1] != 0 and entire_list[element] - 1 != entire_list[element - 1]):
            count = count + 1

    return count
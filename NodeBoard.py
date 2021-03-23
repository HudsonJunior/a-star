class node_board:
        def __init__(self, board_state, position, parent_node):
            self.board_state = board_state
            self.position = position
            self.g_cost = 0
            self.h_cost = 0
            self.parent_node = parent_node
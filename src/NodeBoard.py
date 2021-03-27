class node_board:
        def __init__(self, board_state, white_space, parent_node):
            self.board_state = board_state
            self.white_space = white_space ## Coordenadas onde está a peça em branco
            self.g_cost = 0
            self.h_cost = 0
            self.parent_node = parent_node
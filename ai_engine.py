#
# The Chess AI class
# Will utilize minimax and alpha beta pruning
#
#
# TODO: switch undo moves to stack data structure

class chess_ai:
    '''
    call minimax with alpha beta pruning
    evaluate board
    get the value of each piece
    '''

    def __init__(self):
        pass

    def minimax(self, game_state, depth, alpha, beta, maximizing_player, player_color):
        if depth == 0 or game_state.checkmate_stalemate_checker() != 3:
            return self.evaluate_board(game_state)
        elif maximizing_player:
            max_evaluation = float('-inf')
            all_possible_moves = game_state.get_all_legal_moves(player_color)
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1])
                evaluation = self.minimax(game_state, depth - 1, alpha, beta, False, player_color)
                game_state.move_piece(move_pair[1], move_pair[0])
                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    best_possible_move = move_pair
                max_evaluation = max(evaluation, max_evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            if depth == 3:
                return best_possible_move
            return max_evaluation

        else:
            min_evaluation = float('inf')
            all_possible_moves = game_state.get_all_legal_moves(player_color)
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1])
                evaluation = self.minimax(game_state, depth - 1, alpha, beta, True, player_color)
                game_state.move_piece(move_pair[1], move_pair[0])
                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    best_possible_move = move_pair
                min_evaluation = min(evaluation, min_evaluation)
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            if depth == 3:
                return best_possible_move
            return min_evaluation


    def evaluate_board(self, game_state):
        evaluation_score = 0
        for row in range(0, 8):
            for col in range(0, 8):
                if game_state.is_valid_piece(row, col):
                    evaluated_piece = game_state.get_piece(row, col)
                    evaluation_score += self.get_piece_value(evaluated_piece, evaluated_piece.get_player())
        return evaluation_score

    def get_piece_value(self, piece, player_color):
        if piece.is_player(player_color):
            if piece.get_name() is "k":
                return 1000
            elif piece.get_name() is "q":
                return 100
            elif piece.get_name() is "r":
                return 50
            elif piece.get_name() is "b":
                return 30
            elif piece.get_name() is "n":
                return 30
            elif piece.get_name() is "p":
                return 10
        else:
            if piece.get_name() is "k":
                return -1000
            elif piece.get_name() is "q":
                return -100
            elif piece.get_name() is "r":
                return -50
            elif piece.get_name() is "b":
                return -30
            elif piece.get_name() is "n":
                return -30
            elif piece.get_name() is "p":
                return -10
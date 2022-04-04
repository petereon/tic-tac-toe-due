import random
from typing import List, Tuple, Union
import time


def initialize_game():
    state = {
        "board": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
        "player": "X",
        "status": None,
        "msg": None,
    }
    return state


def get_indexes(board: List[List[str]], value: str) -> List[Tuple[int, int]]:
    indexes = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == value:
                indexes.append((i, j))
    return indexes


def get_random_move(game_state: dict) -> Tuple[int, int]:
    empty_cell_indexes = get_indexes(game_state["board"], ' ')
    return empty_cell_indexes[random.randint(0, len(empty_cell_indexes) - 1)]


def player_wins(game_state: dict, player: str) -> bool:
    all_cells_taken_by_player = get_indexes(game_state["board"], player)
    if len(all_cells_taken_by_player) < 3:
        return False
    cols, rows = list(zip(*all_cells_taken_by_player))
    for i in range(3):
        # Vertical
        if cols.count(i) == 3:
            return True
        # Horizontal
        if rows.count(i) == 3:
            return True

    # Diagonal dexter
    if [abs(i-j) for i, j in all_cells_taken_by_player].count(0) == 3:
        return True
    
    # Diagonal sinister
    if [i+j for i, j in all_cells_taken_by_player].count(3) == 3:
        return True
    

    return False


def assess_game(game_state: dict) -> dict:
    if player_wins(game_state, "X"):
        game_state['status'] = "X"
        game_state['msg'] = "PLAYER X WON!"
    elif player_wins(game_state, "O"):
        game_state['status'] = "O"
        game_state['msg'] = "PLAYER O WON!"
    elif len(get_indexes(game_state["board"], " ")) == 0:
        game_state['status'] = "D"
        game_state['msg'] = "GAME ENDS WITH A DRAW!"
    
    return game_state


def process_move(game_state: dict, move_position: Union[Tuple[int, int], None] = None) -> Tuple[dict, bool]:
    if move_position is None:
        move_position = get_random_move(game_state)
    row, col = (move_position[0], move_position[1])
    if (row >= 3) or (col >= 3):
        game_state["msg"] = "Invalid move, provide a valid position"
        return game_state, False

    if game_state["board"][row][col] != " ":
        game_state["msg"] = "Invalid move, position already taken"
        return game_state, False

    game_state["board"][row][col] = game_state["player"]
    return game_state, True


def process_round(game_state, move_position: Union[Tuple[int, int], None] = None) -> dict:
    game_state, success = process_move(game_state, move_position)
    if success:
        game_state = assess_game(game_state)
    if game_state['player'] == 'X':
        game_state['player'] = 'O'
    else:
        game_state['player'] = 'X'
    return game_state
    


def play_game(sleeptime=2):
    """Put together the game"""
    game_state = initialize_game()


    while game_state['status'] is None:
        game_state = process_round(game_state)
        print(game_state['board'])
        time.sleep(sleeptime)


if __name__ == "__main__":
    play_game()  # pragma: no cover

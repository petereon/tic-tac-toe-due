import random
import time
from typing import List, Tuple, Union

from tic_tac_toe_due.move import process_move
from tic_tac_toe_due.util import get_indexes


def initialize_game():
    state = {
        "board": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
        "player": "X",
        "status": None,
        "msg": None,
    }
    return state


def diagonal_win(all_cells_taken_by_player: List[Tuple[int, int]]) -> bool:

    # Diagonal dexter
    if [abs(i - j) for i, j in all_cells_taken_by_player].count(0) == 3:
        return True

    # Diagonal sinister
    if [i + j for i, j in all_cells_taken_by_player].count(2) == 3:
        return True

    return False


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

    return diagonal_win(all_cells_taken_by_player)


def assess_game(game_state: dict) -> dict:
    if player_wins(game_state, "X"):
        game_state["status"] = "X"
        game_state["msg"] = "PLAYER X WON!"
    elif player_wins(game_state, "O"):
        game_state["status"] = "O"
        game_state["msg"] = "PLAYER O WON!"
    elif len(get_indexes(game_state["board"], " ")) == 0:
        game_state["status"] = "D"
        game_state["msg"] = "GAME ENDS WITH A DRAW!"

    return game_state


def process_round(
    game_state: dict, move_position: Union[Tuple[int, int], None] = None
) -> Tuple[dict, bool]:
    game_state, success = process_move(game_state, move_position)
    if success:
        game_state = assess_game(game_state)
        if game_state["player"] == "X":
            game_state["player"] = "O"
        else:
            game_state["player"] = "X"
    return game_state, success

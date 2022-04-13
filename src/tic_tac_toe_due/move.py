import random
from typing import Tuple, Union

from tic_tac_toe_due.util import get_indexes


def get_random_move(game_state: dict) -> Tuple[int, int]:
    empty_cell_indexes = get_indexes(game_state["board"], " ")
    return empty_cell_indexes[random.randint(0, len(empty_cell_indexes) - 1)]


def is_valid_move(
    game_state: dict, row: int, col: int
) -> Union[Tuple[bool, str], Tuple[bool, None]]:

    if (row >= 3) or (col >= 3):
        return False, "Invalid move, provide a valid position"

    if game_state["board"][row][col] != " ":
        return False, "Invalid move, position already taken"

    return True, None


def process_move(
    game_state: dict, move_position: Union[Tuple[int, int], None] = None
) -> Tuple[dict, bool]:

    if move_position is None:
        move_position = get_random_move(game_state)  # pragma: no cover

    row, col = (move_position[0], move_position[1])

    valid = is_valid_move(game_state, row, col)
    if not valid[0]:
        game_state["msg"] = valid[1]
        return game_state, False

    game_state["board"][row][col] = game_state["player"]
    return game_state, True

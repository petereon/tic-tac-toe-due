import numpy as np
import random
from typing import List, Tuple, Union
import time

player_mapping = {"X": 1, "O": -1, 1: "X", -1: "O", " ": 0, 0: " "}


def initialize_game():
    state = {
        "board": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
        "player": "X",
        "status": None,
        "msg": None,
    }
    return state


def generate_board():
    return np.zeros((3, 3))


def generate_board_repr(board: np.ndarray, endmes: Union[None, str]):
    if (board == np.zeros((3, 3))).all():
        print(
            """Game Board Creation...
 | | 
-+-+-
 | | 
-+-+-
 | | 
Board Created."""
        )
    else:
        turn = len(np.argwhere(board != 0)) % 2

        if turn == 1:
            startmes = "Player X:\n"
        else:
            startmes = "Player O:\n"

        # create board:
        boardmes = ""
        i = 0
        for row in board.tolist():
            i += 1
            boardmes += "|".join([player_mapping[int(player)] for player in row]) + "\n"
            if i != 3:
                boardmes += "-+-+-\n"

        print(startmes + boardmes + "\n\n" + (endmes if endmes is not None else ""))


def player_sign(possible: list, player: str) -> int:
    """
    Give random possible move
    """

    rand_num = random.randint(0, len(possible) - 1)
    return possible[rand_num]


def assess_game(board: np.ndarray, position: int) -> int:
    """
    Assess the game
    """
    row, col = divmod(position - 1, 3)

    player = board[row][col]
    where_player = np.argwhere(board == player)

    # Vertical
    counter = 0
    for i, j in where_player.tolist():
        # Vertical
        if j == col:
            counter += 1
        if counter == 3:
            return player

    # Horizontal
    counter = 0
    for i, j in where_player.tolist():
        if i == row:
            counter += 1
        if counter == 3:
            return player

    # Diagonal
    counter = 0
    for i, j in where_player.tolist():
        if i == j:
            counter += 1
        if counter == 3:
            return player

    if len(np.argwhere(board == 0)) == 0:
        return 0
    else:
        return None


def process_move(game_state: dict, move: List[int]) -> Tuple[dict, bool]:
    row, col = (move[0], move[1])
    if (row >= 3) or (col >= 3):
        game_state["msg"] = "Invalid move, provide a valid position"
        return game_state, False

    if game_state["board"][row][col] != " ":
        game_state["msg"] = "Invalid move, position already taken"
        return game_state, False

    game_state["board"][row][col] = game_state["player"]
    return game_state, True


def process_round(board: np.ndarray, player, turn_position):  # eg. pick square with id 7
    row, col = divmod(turn_position - 1, 3)  # check
    board[row][col] = player
    game_status = assess_game(board, turn_position)
    if game_status == 1:
        endmes = "PLAYER X WON!"
    elif game_status == -1:
        endmes = "PLAYER O WON!"
    elif game_status == 0:
        endmes = "GAME ENDS WITH A DRAW!"
    else:
        endmes = None
    generate_board_repr(board, endmes)
    return board, game_status


def play_game(sleeptime=2):
    """Put together the game"""

    board = generate_board()
    generate_board_repr(board, None)

    player = 1
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_status = None

    while game_status is None:
        turn_position = player_sign(possible, player_mapping[player])
        possible.remove(turn_position)
        board, game_status = process_round(board, player, turn_position)
        player = player * (-1)
        time.sleep(sleeptime)


if __name__ == "__main__":
    play_game()  # pragma: no cover

from pytest_bdd import scenario, given, when, then, parsers
from tic_tac_toe_due import generate_board, process_round

import numpy as np
import json

from expycted import expect


@scenario("move.features", "Player makes an invalid move")
def test_making_an_invalid_move():
    pass


@scenario("move.features", "Player makes a valid move")
def test_making_a_valid_move():
    pass


@scenario("move.features", "Player makes a move out of board")
def test_making_out_of_board_move():
    pass


@scenario("endgame.features", "Player 1 wins")
def test_player_1_win():
    pass


@scenario("endgame.features", "Player -1 wins")
def test_player_minus_1_win():
    pass


@scenario("endgame.features", "Game is a tie")
def test_game_is_a_tie():
    pass


@given("a game is in progress", target_fixture="board")
def game_is_in_progress():
    return generate_board()


@given(parsers.parse("the current player is {player}"), target_fixture="player")
def the_player(player):
    return player


@given(
    parsers.parse("square {coord} is unoccupied"),
    target_fixture="board",
    converters={"coord": int},
)
def a_square_is_unoccupied(board, coord):
    row, col = divmod(coord - 1, 3)
    board[row][col] = 0
    return board


@given(
    parsers.parse("square {coord} is occupied"), target_fixture="board", converters={"coord": int}
)
def a_square_is_occupied(board, coord):
    row, col = divmod(coord - 1, 3)
    board[row][col] = 1
    return board


@given(
    parsers.parse("the board is {board}"), target_fixture="board", converters={"board": json.loads}
)
def the_board_is(board):
    return np.array(board)


@when(
    parsers.parse("player makes a move at {coord}"),
    target_fixture="result",
    converters={"coord": int},
)
def a_player_makes_move_at_square(board, player, coord):
    try:
        board, game_status = process_round(board, player, coord)
        return board, game_status
    except Exception as e:
        return None, e


@then(parsers.parse("square {coord} is occupied by {player}"), converters={"coord": int})
def a_square_is_occupied_by_a_player(result, coord, player):
    row, col = divmod(coord - 1, 3)
    expect(int(result[0][row][col])).to.equal(int(player))


@then("the game breaks")
def the_game_breaks(result):
    expect(result[0]).to.be(None)
    expect(result[1]).to_not.be(None)


@then(parsers.parse("the winner is {player}"))
def the_winner_is(result, player):
    expect(int(result[1])).to.equal(int(player))

from pytest_bdd import scenario, given, when, then, parsers
from tic_tac_toe_due import generate_board, process_round

import numpy as np
import json

from expycted import expect


@scenario("behavior.features", "Player makes an invalid move")
def test_making_an_invalid_move():
    pass


@scenario("behavior.features", "Player makes a valid move")
def test_making_a_valid_move():
    pass


@scenario("behavior.features", "Player makes a move out of board")
def test_making_out_of_board_move():
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


@when(
    parsers.parse("player makes a move at {coord}"),
    target_fixture="result",
    converters={"coord": int},
)
def a_player_makes_move_at_square(board, player, coord):
    try:
        board, game_status = process_round(board, player, coord)
        return board, None
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

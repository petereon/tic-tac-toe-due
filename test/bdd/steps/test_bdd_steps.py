from pytest_bdd import scenario, given, when, then, parsers
from tic_tac_toe_due import initialize_game, process_round

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


@scenario("endgame.features", "Player X wins")
def test_player_1_win():
    pass


@scenario("endgame.features", "Player O wins")
def test_player_minus_1_win():
    pass


@scenario("endgame.features", "Game is a tie")
def test_game_is_a_tie():
    pass


@given("a game is in progress", target_fixture="state")
def game_is_in_progress():
    return initialize_game()


@given(parsers.parse("the current player is {player}"), target_fixture="state")
def the_player(player,state):
    state["player"] = player
    return state


@given(
    parsers.parse("square {coord} is unoccupied"),
    target_fixture="state",
    converters={"coord": json.loads},
)
def a_square_is_unoccupied(state, coord):
    row, col = (coord[0], coord[1])
    state['board'][row][col] = ' '
    return state


@given(
    parsers.parse("square {coord} is occupied"), target_fixture="state", converters={"coord": json.loads}
)
def a_square_is_occupied(state, coord):
    row, col = (coord[0], coord[1])
    state['board'][row][col] = 'X'
    return state



@given(
    parsers.parse("the board is {board}"), target_fixture="state", converters={"board": json.loads}
)
def the_board_is(board, state):
    state['board'] = board
    return state


@when(
    parsers.parse("player makes a move at {coord}"),
    target_fixture="result",
    converters={"coord": json.loads},
)
def a_player_makes_move_at_square(state, coord):
    return process_round(state, coord)


@then("board remains unchanged")
def board_remains_unchanged(state, result):
    assert result == state


@then(parsers.parse("message is {message}"))
def message_is(message, result):
    assert '"{}"'.format(result['msg']) == message


@then(parsers.parse("square {coord} is occupied by {player}"), converters={"coord": json.loads})
def a_square_is_occupied_by_a_player(result, coord, player):
    row, col = (coord[0], coord[1])
    assert result['board'][row][col] == player


@then(parsers.parse("the winner is {player}"))
def the_winner_is(result, player):
    result['status'] = player


@then("the game is a tie")
def the_game_is_a_tie(result):
    assert result['status'] == 'D'

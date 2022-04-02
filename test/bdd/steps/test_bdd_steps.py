from pytest_bdd import scenario, given, when, then, parsers
from tic_tac_tue_due import process_round
import json

from expycted import expect


@scenario("behavior.features", "Player makes a valid move")
def test_making_a_move():
    pass


@given("a game is in progress", target_fixture="game_state")
def game_is_in_progress():
    game_state = {}
    game_state["game_status"] = None
    return game_state


@given(parsers.parse("the current player is {player}"), target_fixture="game_state")
def the_player(game_state, player):
    game_state["current_player"] = player
    return game_state


@given(
    parsers.parse("square {coord} is unoccupied"),
    target_fixture="game_state",
    converters={"coord": json.loads},
)
def a_square_is_unoccupied(game_state, coord):
    game_state["board"] = [["X", " ", "O"], [" ", " ", " "], [" ", " ", " "]]
    game_state["board"][coord[0]][coord[1]] = " "
    return game_state


@when(
    parsers.parse("player makes a move at {coord}"),
    target_fixture="game_state",
    converters={"coord": json.loads},
)
def a_player_makes_move_at_square(game_state, coord):
    game_state = process_round(game_state, coord)
    return game_state


@then(parsers.parse("square {coord} is occupied by {player}"), converters={"coord": json.loads})
def a_square_is_occupied_by_a_player(game_state, coord, player):
    expect(game_state["board"][coord[0]][coord[1]]).to.be_equal_to(player)


@then("the player is {player}")
def the_player_then(game_state, player):
    expect(game_state["current_player"]).to.be_equal_to(player)

from pytest_bdd import scenario, given, when, then


@scenario("behavior.features", "Player makes a valid move")
def test_making_a_move():
    pass


@given("a game is in progress")
def game_is_in_progress():
    assert False


@given('the player is "X"')
def the_player():
    assert False


@given("square [0,1] is unoccupied")
def a_square_is_unoccupied():
    assert False


@when("player makes a move at [0,1]")
def a_player_makes_move_at_square():
    assert False


@then('square [0,1] is occupied by "X"')
def a_square_is_occupied_by_a_player():
    assert False


@then('the player is "O"')
def the_player_then():
    the_player()

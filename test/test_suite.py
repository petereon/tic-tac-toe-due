from tic_tac_toe_due import *
import pytest


@pytest.fixture
def get_example_game_state():
    return {
        "board": [["X", "O", " "], ["X", "X", " "], [" ", " ", "O"]],
        "player": "O",
        "status": None,
        "msg": None,
    }


@pytest.fixture
def get_empty_board():
    """
    Generate a board
    """
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


@pytest.fixture
def get_example_board():
    """
    Generate a board
    """
    return [["X", "O", "X"], ["X", "O", " "], [" ", "O", " "]]


@pytest.fixture
def get_diagonal_win_board():
    """
    Generate a board
    """
    return [["O", "X", "X"], ["X", "O", " "], [" ", "O", "O"]]


def test_get_indexes(get_example_board):
    assert get_indexes(get_example_board, " ") == [(1, 2), (2, 0), (2, 2)]
    assert get_indexes(get_example_board, "X") == [(0, 0), (0, 2), (1, 0)]
    assert get_indexes(get_example_board, "O") == [(0, 1), (1, 1), (2, 1)]


def test_get_random_move(get_example_game_state):
    state = get_example_game_state
    get_random_move(state) in [(1, 2), (0, 0), (2, 0)]


def describe_assess_game():
    def test_player_1_wins(get_example_game_state):
        state = get_example_game_state
        state["board"] = [["X", "O", "X"], ["X", "O", " "], ["X", " ", " "]]

        assert assess_game(state)["status"] == "X"

    def test_player_minus_1_wins(get_example_game_state):
        state = get_example_game_state
        state["board"] = [["X", "O", "X"], ["X", "O", " "], [" ", "O", " "]]

        assert assess_game(state)["status"] == "O"

    def test_player_minus_1_diag_win(get_example_game_state):
        state = get_example_game_state
        state["board"] = [["X", "O", "X"], ["O", "X", " "], ["X", "O", "O"]]
        assert assess_game(state)["status"] == "X"


def describe_process_round():
    def test_player_1_wins(get_example_game_state):
        state = get_example_game_state
        state["board"] = [["X", "O", "X"], ["X", "O", " "], [" ", " ", " "]]
        state["player"] = "X"
        state = process_round(state, (2, 0))
        assert state["board"] == [["X", "O", "X"], ["X", "O", " "], ["X", " ", " "]]
        assert state["status"] == "X"

    def test_player_minus_1_wins(get_example_game_state):
        state = get_example_game_state
        state["board"] = [["X", "O", "X"], ["X", "O", " "], [" ", " ", " "]]
        state = process_round(state, (2, 1))
        assert state["board"] == [["X", "O", "X"], ["X", "O", " "], [" ", "O", " "]]
        assert state["status"] == "O"

    def test_player_minus_1_diag_win(get_example_game_state):
        state = get_example_game_state
        state["board"] = [["X", "O", "X"], ["O", "X", " "], [" ", " ", " "]]
        state["player"] = "X"
        state = process_round(state, (2, 2))
        assert state["board"] == [["X", "O", "X"], ["O", "X", " "], [" ", " ", "X"]]
        assert state["status"] == "X"


def describe_process_move():
    def test_valid_move_is_made(get_example_game_state):
        state = get_example_game_state
        state, valid = process_move(state, (1, 2))

        assert state["board"][1][2] == "O"
        assert valid == True
        assert state["msg"] == None

    def test_invalid_move_is_made(get_example_game_state):
        state = get_example_game_state
        new_state, valid = process_move(state, (1, 1))

        assert new_state == state
        assert valid == False
        assert new_state["msg"] == None

    def test_out_of_board_move_is_made(get_example_game_state):
        state = get_example_game_state
        new_state, valid = process_move(state, (5, 2))

        assert new_state == state
        assert valid == False
        assert new_state["msg"] == None

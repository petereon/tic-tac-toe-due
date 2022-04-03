from tic_tac_toe_due import *
import pytest

from expycted import expect


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
    return np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])


@pytest.fixture
def get_example_board():
    """
    Generate a board
    """
    return np.array([[1, -1, 1], [1, -1, 0], [0, -1, 0]])


@pytest.fixture
def get_diagonal_win_board():
    """
    Generate a board
    """
    return np.array([[-1, 1, 1], [1, -1, 0], [0, -1, -1]])


def test_generate_board():
    board = generate_board()
    expect(board.shape).to.be((3, 3))
    assert np.all(board == 0)


def describe_generate_board_repr():
    def test_repr_empty_board(get_empty_board, capsys):
        board = get_empty_board
        generate_board_repr(board, None)

        assert (
            capsys.readouterr().out.replace("\n", "")
            == """Game Board Creation...
 | | 
-+-+-
 | | 
-+-+-
 | | 
Board Created.""".replace(
                "\n", ""
            )
        )

    def test_repr_board_with_data(get_example_board, capsys):
        board = get_example_board
        generate_board_repr(board, None)

        assert (
            capsys.readouterr().out.replace("\n", "")
            == """Player O:
X|O|X
-+-+-
X|O| 
-+-+-
 |O| 
""".replace(
                "\n", ""
            )
        )

    def test_repr_board_with_data_and_endmes(get_example_board, capsys):
        board = get_example_board
        generate_board_repr(board, "Fero vyhral!")

        assert (
            capsys.readouterr().out.replace("\n", "")
            == """Player O:
X|O|X
-+-+-
X|O| 
-+-+-
 |O| 
Fero vyhral!""".replace(
                "\n", ""
            )
        )


def test_player_sign():
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert player_sign(possible, "X") in possible
    assert player_sign(possible, "O") in possible


def describe_assess_game():
    def test_player_1_wins(get_example_board):
        board = get_example_board
        board[2][0] = 1
        assert assess_game(board, 7) == 1

    def test_player_minus_1_wins(get_example_board):
        board = get_example_board
        assert assess_game(board, 8) == -1

    def test_player_minus_1_diag_win(get_diagonal_win_board):
        board = get_diagonal_win_board
        assert assess_game(board, 9) == -1


def describe_process_round():
    def test_player_1_wins(get_example_board):
        board = get_example_board
        end_board = board.copy()
        end_board[2][0] = 1
        result = process_round(board, 1, 7)
        assert (result[0] == end_board).all()
        assert result[1] == 1

    def test_player_minus_1_wins(get_example_board):
        board = get_example_board
        end_board = board.copy()
        board[2][1] = 0
        result = process_round(board, -1, 8)
        assert (result[0] == end_board).all()
        assert result[1] == -1

    def test_player_minus_1_diag_win(get_diagonal_win_board):
        board = get_diagonal_win_board
        end_board = board.copy()
        board[2][2] = 0
        result = process_round(board, -1, 9)
        assert (result[0] == end_board).all()
        assert result[1] == -1


def test_play_game(capsys):
    play_game(0)
    prints = capsys.readouterr().out

    assert "Player X:" in prints
    assert "Player O:" in prints
    assert """Game Board Creation...
 | | 
-+-+-
 | | 
-+-+-
 | | 
Board Created.""".replace(
        "\n", ""
    ) in prints.replace(
        "\n", ""
    )


def describe_process_move():
    def test_valid_move_is_made(get_example_game_state):
        state = get_example_game_state
        state, valid = process_move(state, [1, 2])

        expect(state["board"][1][2]).to.be_equal_to("O")
        expect(valid).to.be_equal_to(True)
        expect(state["msg"]).to.be_equal_to(None)

    def test_invalid_move_is_made(get_example_game_state):
        state = get_example_game_state
        new_state, valid = process_move(state, [1, 1])

        expect(new_state).to.be_equal_to(state)
        expect(valid).to.be_equal_to(False)
        expect(new_state["msg"]).to_not.be_equal_to(None)

    def test_out_of_board_move_is_made(get_example_game_state):
        state = get_example_game_state
        new_state, valid = process_move(state, [5, 2])

        expect(new_state).to.be_equal_to(state)
        expect(valid).to.be_equal_to(False)
        expect(new_state["msg"]).to_not.be_equal_to(None)

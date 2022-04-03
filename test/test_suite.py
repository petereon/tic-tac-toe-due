from tic_tac_toe_due import *
import pytest

from expycted import expect


def test_generate_board():
    board = generate_board()
    expect(board.shape).to.be((3, 3))
    assert np.all(board == 0)


def describe_generate_board_repr():
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

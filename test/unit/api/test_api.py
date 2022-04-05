from fastapi.testclient import TestClient
import pytest

from tic_tac_toe_due.api import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture
def get_example_game_state():
    return {
        "board": [["X", "O", " "], ["X", "X", " "], [" ", " ", "O"]],
        "player": "O",
        "status": None,
        "msg": None,
    }


@pytest.mark.parametrize(
    ("id"),
    [(1,), (2,), (3,)],
)
def test_get_new_game(client, id):
    response = client.get("/game/new_game")
    assert response.status_code == 200
    assert response.json() == {
        "id": id,
        "state": {
            "board": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            "player": "X",
            "status": None,
            "msg": None,
        },
    }


def describe_post_move():
    def valid_move(client):
        response = client.post("/game/{game_id}/move")
        assert response.status_code == 200
        assert response.json() == {
            "board": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            "player": "X",
            "status": None,
            "msg": None,
        }

    def invalid_move(client):
        response = client.post("/game/{game_id}/move")
        assert response.status_code == 400
        assert response.json() == {
            "board": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            "player": "X",
            "status": None,
            "msg": "Invalid move",
        }


def describe_get_state():
    def valid_state_id(client):
        response = client.get("/game/{game_id}/state")
        assert response.status_code == 200
        assert response.json() == {
            "board": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            "player": "X",
            "status": None,
            "msg": None,
        }

    def invalid_game_id(client):
        response = client.get("/game/{game_id}/state")
        assert response.status_code == 404
        assert response.json() == {
            "board": None,
            "player": None,
            "status": None,
            "msg": "No such game",
        }

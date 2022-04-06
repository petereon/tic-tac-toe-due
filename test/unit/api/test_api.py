from fastapi.testclient import TestClient
import pytest

from tic_tac_toe_due.api import app, games


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture
def get_example_game_state():
    games["1"] = {
        "board": [["X", "O", " "], ["X", "X", " "], [" ", " ", "O"]],
        "player": "O",
        "status": None,
        "msg": None,
    }

    yield "1"

    del games["1"]


def describe_get_new_game():
    def test_get_new_game(client: TestClient):
        ids = []
        for i in range(10):
            response = client.get("/game/new_game")
            assert response.status_code == 200
            state = response.json()
            ids.append(state["id"])
            del state["id"]

            assert state == {
                "state": {
                    "board": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
                    "player": "X",
                    "status": None,
                    "msg": None,
                },
            }
        assert len(ids) == len(set(ids))


def describe_post_move():
    def valid_move(client: TestClient, get_example_game_state: dict):
        response = client.post(f"/game/{get_example_game_state}/move", data='{"move":[0,2]}')
        assert response.status_code == 200
        assert response.json() == {
            "board": [["X", "O", "O"], ["X", "X", " "], [" ", " ", "O"]],
            "player": "X",
            "status": None,
            "msg": None,
        }

    def invalid_move_out_of_board(client: TestClient, get_example_game_state: dict):
        response = client.post(f"/game/{get_example_game_state}/move", data='{"move":[5,2]}')
        assert response.status_code == 400
        assert response.json() == {
            "board": [["X", "O", " "], ["X", "X", " "], [" ", " ", "O"]],
            "player": "O",
            "status": None,
            "msg": "Invalid move, provide a valid position",
        }

    def invalid_move_taken_cell(client: TestClient, get_example_game_state: dict):
        response = client.post(f"/game/{get_example_game_state}/move", data='{"move":[0,1]}')
        assert response.status_code == 400
        assert response.json() == {
            "board": [["X", "O", " "], ["X", "X", " "], [" ", " ", "O"]],
            "player": "O",
            "status": None,
            "msg": "Invalid move, position already taken",
        }


def describe_get_state():
    def valid_game_id(client: TestClient, get_example_game_state: dict):
        response = client.get(f"/game/{get_example_game_state}/state")
        assert response.status_code == 200
        assert response.json() == {
            "board": [["X", "O", " "], ["X", "X", " "], [" ", " ", "O"]],
            "player": "O",
            "status": None,
            "msg": None,
        }

    def invalid_game_id(client: TestClient):
        response = client.get("/game/1234/state")
        assert response.status_code == 404
        assert response.json() == {
            "board": None,
            "player": None,
            "status": None,
            "msg": "No such game",
        }

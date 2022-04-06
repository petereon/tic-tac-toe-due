from fastapi import FastAPI, Response, status
from typing import Tuple

from uuid import uuid4

from pydantic import BaseModel

from tic_tac_toe_due import *

app = FastAPI()


class Move(BaseModel):
    move: Tuple[int, int]


games = {}


@app.get("/game/new_game")
async def get_new_game():
    global games
    state = initialize_game()
    game_id = uuid4().hex
    games[game_id] = state

    return {"id": game_id, "state": state}


@app.post("/game/{game_id}/move")
async def post_move(game_id: str, response: Response, move: Union[None, Move] = None):
    global games
    state = games[game_id]
    state, valid = process_round(state, move.move if not move is None else move)
    if not valid:
        response.status_code = status.HTTP_400_BAD_REQUEST
    games[game_id] = state

    return state


@app.get("/game/{game_id}/state")
async def get_state(game_id: str, response: Response):
    global games
    state = games.get(game_id, False)
    if state == False:
        state = {
            "board": None,
            "player": None,
            "status": None,
            "msg": "No such game",
        }
        response.status_code = status.HTTP_404_NOT_FOUND
    return state

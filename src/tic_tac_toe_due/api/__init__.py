from fastapi import FastAPI

from tic_tac_toe_due import *

app = FastAPI()


@app.get("/game/new_game")
def get_new_game():
    pass


@app.post("/game/{game_id}/move")
def post_move(game_id):
    pass


@app.get("/game/{game_id}/state")
def get_state(game_id):
    pass

from fastapi import FastAPI
from pydantic import BaseModel
from mines_logic import predict_mines

app = FastAPI()

class GameInput(BaseModel):
    seed: str
    client_seed: str
    nonce: int
    mines: int

@app.post("/predict")
def predict(game: GameInput):
    board = predict_mines(
        seed=game.seed,
        client_seed=game.client_seed,
        nonce=game.nonce,
        mine_count=game.mines
    )
    return {"predicted_board": board
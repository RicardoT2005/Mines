import random

def predict_mines(seed: str, client_seed: str, nonce: int, mine_count: int):
    random.seed(f"{seed}:{client_seed}:{nonce}")
    positions = list(range(25))
    mines = random.sample(positions, mine_count)

    board = [["safe" for _ in range(5)] for _ in range(5)]
    for m in mines:
        row = m // 5
        col = m % 5
        board[row][col] = "mine"

    return board
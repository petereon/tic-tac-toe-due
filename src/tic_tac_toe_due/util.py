from typing import List, Tuple


def get_indexes(board: List[List[str]], value: str) -> List[Tuple[int, int]]:
    indexes = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == value:
                indexes.append((i, j))
    return indexes

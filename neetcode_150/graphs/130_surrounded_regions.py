from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        # inner O's
        inner_os = set()

        # border O's
        border_os = []

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == 'O':
                    border_os.append((r, c))
                elif board[r][c] == 'O':
                    inner_os.add((r, c))

        visited = set()

        # dfs will traverse Os in depth and remove all matches in inner_os
        def dfs(i, j: int):
            if min(i, j) < 0 or i == rows or j == cols or (i, j) in visited or board[i][j] != "O":
                return

            visited.add((i, j))
            if (i, j) in inner_os:
                inner_os.remove((i, j))

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        # dfs to every border O's
        for br, bc in border_os:
            dfs(br, bc)

        # flip all inner O's
        for ir, ic in inner_os:
            board[ir][ic] = 'X'

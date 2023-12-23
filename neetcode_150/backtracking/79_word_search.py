from collections import deque
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        first = word[0]
        rows, cols = len(board), len(board[0])

        starts = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == first:
                    starts.append((i, j))

        def dfs(r, c, cur, v) -> bool:
            if cur >= len(word) or (r, c) in v or board[r][c] != word[cur]:
                return False

            if cur == len(word) - 1 and word[cur] == board[r][c]:
                return True

            v.add((r, c))
            adj = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for ar, ac in adj:
                dr, dc = r + ar, c + ac
                if min(dr, dc) < 0 or dr >= rows or dc >= cols:
                    continue
                if dfs(dr, dc, cur + 1, v):
                    return True

            v.remove((r, c))
            return False

        for si, sj in starts:
            visited = set()
            if dfs(si, sj, 0, visited):
                return True

        return False


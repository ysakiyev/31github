from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q = deque()
        rows = len(rooms)
        cols = len(rooms[0])

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append([i, j])

        while q:
            cur = q.popleft()
            adj = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for r, c in adj:
                dr, dc = cur[0] + r, cur[1] + c
                if not 0 <= dr < rows or not 0 <= dc < cols or rooms[dr][dc] == -1 or rooms[dr][dc] == 0:
                    continue
                if rooms[dr][dc] > rooms[cur[0]][cur[1]] + 1:
                    rooms[dr][dc] = rooms[cur[0]][cur[1]] + 1
                    q.append([dr, dc])

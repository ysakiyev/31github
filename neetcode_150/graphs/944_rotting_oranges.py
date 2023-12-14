from collections import deque
from typing import List
import copy


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            len_q = len(q)
            for i in range(len_q):
                rr, rc = q.popleft()
                neighbors = [(rr + 1, rc), (rr - 1, rc), (rr, rc + 1), (rr, rc - 1)]
                for nr, nc in neighbors:
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1


s = Solution()
print(s.orangesRotting([[0]]))

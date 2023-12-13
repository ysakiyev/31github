from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c) -> int:
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            area = 1

            area += dfs(r + 1, c)
            area += dfs(r, c + 1)
            area += dfs(r - 1, c)
            area += dfs(r, c - 1)

            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    cur_area = dfs(i, j)
                    max_area = max(max_area, cur_area)

        return max_area


s = Solution()
print(s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))

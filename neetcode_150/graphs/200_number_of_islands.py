from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == "0":
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    counter += 1
                    dfs(i, j)

        return counter


s = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(s.numIslands(grid))
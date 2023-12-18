from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visit) -> (int, int):
            if (r, c) in visit:
                return

            visit.add((r, c))
            neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for nr, nc in neighbours:
                dr, dc = r + nr, c + nc
                if 0 <= dr < rows and 0 <= dc < cols and heights[dr][dc] >= heights[r][c]:
                    dfs(dr, dc, visit)

        for i in range(cols):
            dfs(0, i, pacific)
            dfs(rows - 1, i, atlantic)

        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)

        # result is intersection of sets
        res = list(pacific.intersection(atlantic))

        return res


s = Solution()
print(s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))

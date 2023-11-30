from typing import List


class Solution:
    def getRowCol(self, i, m: int) -> []:
        row = i // m
        col = i % m

        return [row, col]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        left, right = 0, n * m - 1

        while left <= right:
            mid = left + (right - left) // 2
            rc = self.getRowCol(mid, m)
            val = matrix[rc[0]][rc[1]]

            if val == target:
                return True
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

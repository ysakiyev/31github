from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[{} for _ in range(3)] for _ in range(3)]
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == ".":
                    continue

                # check rows
                if val in rows[i]:
                    return False
                else:
                    rows[i][val] = True

                # check cols
                if val in cols[j]:
                    return False
                else:
                    cols[j][val] = True

                # check boxes
                bi = i // 3
                bj = j // 3

                if val in boxes[bi][bj]:
                    return False
                else:
                    boxes[bi][bj][val] = True
        return True

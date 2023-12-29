from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_p, closed_p, str_p):
            if open_p == closed_p == n:
                res.append(str_p)
                return

            if open_p < n:
                str_p += "("
                backtrack(open_p + 1, closed_p, str_p)
                str_p = str_p[:len(str_p) - 1]

            if closed_p < open_p:
                str_p += ")"
                backtrack(open_p, closed_p + 1, str_p)
                str_p = str_p[:len(str_p) - 1]

        backtrack(0, 0, "")
        return res


s = Solution()
print(s.generateParenthesis(3))

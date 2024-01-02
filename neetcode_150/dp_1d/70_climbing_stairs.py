class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(m: int):
            if m < 0:
                return 0
            if m == 0:
                return 1

            if m-1 not in memo:
                memo[m-1] = climb(m - 1)

            if m-2 not in memo:
                memo[m-2] = climb(m - 2)

            return memo[m-1] + memo[m-2]

        return climb(n)

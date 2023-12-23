from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(candidates, nums):
            if sum(nums) == target:
                res.append(nums.copy())

            if sum(nums) > target:
                return

            for i in range(len(candidates)):
                nums.append(candidates[i])
                dfs(candidates[i:], nums)
                nums.pop()

        dfs(candidates, [])
        return res


s = Solution()
print(s.combinationSum([2, 3, 5], 8))

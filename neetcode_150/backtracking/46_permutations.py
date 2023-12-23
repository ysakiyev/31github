from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(nums, perm):
            if len(perm) == n:
                res.append(perm)
                return

            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], perm + [nums[i]])

        backtrack(nums, [])
        return res


s = Solution()
print(s.permute([1, 2, 3]))
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

s = Solution()
print(s.subsetsWithDup([1,2,2]))
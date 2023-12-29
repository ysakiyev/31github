from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = n - 2

        reach = n - 1
        while i >= 0:
            if nums[i] >= reach - i:
                reach = i
            i -= 1

        return reach == 0




from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        jumps = 0

        while r < len(nums) - 1:
            max_jump = 0
            for i in range(l, r+1):
                max_jump = max(max_jump, i + nums[i])
            l = r + 1
            r = max_jump
            jumps += 1

        return jumps
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max, cur_min = 0, 0
        global_max, global_min = nums[0], nums[0]
        total_sum = 0

        for n in nums:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)

            global_max = max(global_max, cur_max)
            global_min = min(global_min, cur_min)
            total_sum += n

        return max(global_max, total_sum - global_min) if global_max > 0 else global_max
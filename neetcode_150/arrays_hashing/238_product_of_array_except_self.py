from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        suffix = nums.copy()

        for i in range(1, len(prefix)):
            prefix[i] *= prefix[i - 1]

        for i in reversed(range(0, len(suffix)-1)):
            suffix[i] *= suffix[i + 1]

        nums[0] = suffix[1]
        nums[len(nums) - 1] = prefix[len(nums) - 2]

        for i in range(1, len(nums) - 1):
            nums[i] = prefix[i - 1] * suffix[i + 1]

        return nums

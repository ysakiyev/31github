from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        cur_min = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                cur_min = min(cur_min, nums[left])
                break

            mid = left + (right - left) // 2
            cur_min = min(cur_min, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return cur_min


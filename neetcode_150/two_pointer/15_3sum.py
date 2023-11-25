from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        cur = 0
        while cur < len(nums):
            if cur > 0 and nums[cur - 1] == nums[cur]:
                cur += 1
                continue

            left, right = cur + 1, len(nums) - 1

            while left < right:
                sum_3 = nums[cur] + nums[left] + nums[right]
                if sum_3 == 0:
                    res.append([nums[cur], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sum_3 > 0:
                    right -= 1
                else:
                    left += 1
            cur += 1

        return res


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # -4 -1 -1 0 1 2

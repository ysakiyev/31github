from typing import List

# Since the input array is sorted, we can use two pointers left/right to start from start/end of array.
# If sum nums[left] + nums[right] < target, then left++
# else if sum nums[left] + nums[right] > target, then right--
# else add left,right to res

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

            while numbers[left] + numbers[right] > target:
                right -= 1

            while numbers[left] + numbers[right] < target:
                left += 1

        return []
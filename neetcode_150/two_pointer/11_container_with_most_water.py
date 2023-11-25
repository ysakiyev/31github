from typing import List

# The idea is to start with two pointers - leftmost and rightmost, because we want to use the max width we can.
# Then for each iteration, depending on which left/right height is less, move it.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = self.calc_area(height, left, right)

        while left < right:
            area = self.calc_area(height, left, right)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1

            if area > max_area:
                max_area = area

        return max_area

    def calc_area(self, height, left, right):
        return min(height[left], height[right]) * (right - left)


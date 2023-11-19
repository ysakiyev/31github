# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h_set = set()
        for n in nums:
            if n in h_set:
                return True
            h_set.add(n)

        return False


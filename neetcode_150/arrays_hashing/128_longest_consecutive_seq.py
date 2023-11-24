from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        hset = set()
        for n in nums:
            hset.add(n)

        longest = 0
        cur = 1

        for n in nums:
            # not beginning of sequence
            if (n - 1) in hset:
                continue

            i = 1
            while (n + i) in hset:
                cur += 1
                i += 1

            if cur > longest:
                longest = cur

            cur = 1

        return longest

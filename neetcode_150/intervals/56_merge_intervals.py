from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        i = 0
        while i < len(intervals):
            cur = intervals[i]
            max_right = cur[1]
            while i < len(intervals) - 1 and max_right >= intervals[i + 1][0]:
                i += 1
                if intervals[i][1] > max_right:
                    max_right = intervals[i][1]
            res.append([cur[0], max_right])
            i += 1

        return res

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_int: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if new_int[1] < start:      # new interval is before current
                res.append(new_int)
                return res + intervals[i:]
            elif new_int[0] > end:      # new interval is after current
                res.append(intervals[i])
            else:                       # new interval overlaps
                new_int = [min(new_int[0], start), max(new_int[1], end)]

        res.append(new_int)
        return res

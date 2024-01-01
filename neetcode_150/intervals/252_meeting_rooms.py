from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort()

        prev = intervals[0]

        for start, end in intervals[1:]:
            if prev[1] <= start:
                prev = [start, end]
                continue
            else:
                return False

        return True
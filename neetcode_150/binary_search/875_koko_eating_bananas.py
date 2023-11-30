import math
from typing import List


class Solution:
    def calc_hours(self, piles: List[int], speed: int) -> int:
        hours = 0
        for p in piles:
            hours += math.ceil(p/speed)

        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        if len(piles) == h:
            return max_pile

        speed_start = 1
        speed_end = max_pile

        min_speed = max_pile

        while speed_start <= speed_end:
            speed_mid = speed_start + (speed_end - speed_start) // 2
            hours = self.calc_hours(piles, speed_mid)

            if hours <= h:
                speed_end = speed_mid - 1
                min_speed = speed_mid
            else:
                speed_start = speed_mid + 1

        return min_speed


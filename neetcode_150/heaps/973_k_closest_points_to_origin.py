import math
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(-math.sqrt(point[0]*point[0] + point[1]*point[1]), point) for point in points]
        heapq.heapify(dists)

        while len(dists) > k:
            heapq.heappop(dists)

        return [dist[1] for dist in dists]

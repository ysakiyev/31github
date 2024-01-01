from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_neg = [-stone for stone in stones]
        heapq.heapify(stones_neg)
        self.heap = stones_neg

        while len(self.heap) > 1:
            x = heapq.heappop(self.heap)
            y = heapq.heappop(self.heap)

            diff = x - y
            if diff != 0:
                heapq.heappush(self.heap, -abs(diff))

        if len(self.heap) == 0:
            return 0
        return -self.heap[0]
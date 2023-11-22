import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        dl = list(d.items())

        heapq.heapify(dl)
        k_most_freq = heapq.nlargest(k, dl, key=lambda x: x[1])
        res = [tpl[0] for tpl in k_most_freq]
        return res


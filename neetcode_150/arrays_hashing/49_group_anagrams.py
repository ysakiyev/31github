from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []

        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in d:
                d[s_sorted] = [s]
            else:
                d[s_sorted].append(s)

        for k, v in d.items():
            res.append(v)

        return res

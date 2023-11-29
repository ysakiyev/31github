from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, speed) for pos, speed in zip(position, speed)]
        pairs.sort(reverse=True)

        st = []
        for p, s in pairs:
            t = (target - p) / s
            if not st:
                st.append(t)
            else:
                if t > st[-1]:
                    st.append(t)

        return len(st)


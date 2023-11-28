from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0 for _ in range(len(temperatures))]
        for i, v in enumerate(temperatures):
            if i == 0:
                st.append([v,i])
                continue

            while st and v > st[-1][0]:
                top = st.pop()
                res[top[1]] = i - top[1]
            st.append([v, i])

        return res


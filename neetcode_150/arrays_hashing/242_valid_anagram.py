class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = {}
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1

        for c in t:
            if c in m:
                m[c] -= 1
                if m[c] == 0:
                    del m[c]
            else:
                return False

        return True

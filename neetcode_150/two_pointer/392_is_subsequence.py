class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)

        j = 0
        for i in range(len_s):
            while j < len_t and t[j] != s[i]:
                j += 1
            if j == len_t or t[j] != s[i]:
                return False
            j += 1

        return True

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for c in s1:
            if c in hmap:
                hmap[c] += 1
            else:
                hmap[c] = 1

        left, right = 0, len(s1) - 1

        while right < len(s2):
            start, end = left, right
            copy_hmap = hmap.copy()
            for i in range(start, end+1):
                cur = s2[i]
                if cur not in copy_hmap:
                    break
                else:
                    copy_hmap[cur] -= 1
                    if copy_hmap[cur] == 0:
                        del copy_hmap[cur]
                    if len(copy_hmap) == 0:
                        return True
            left += 1
            right += 1

        return False

s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))
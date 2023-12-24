class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        n = len(s)
        longest = 1
        left, right = 0, 0
        substr = set()

        while right < n:
            if s[right] in substr:
                substr.remove(s[left])
                left += 1
                continue

            substr.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1

        return longest


s = Solution()
print(s.lengthOfLongestSubstring("abba"))






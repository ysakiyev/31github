class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        for right in range(len(s)):
            # increase count for current letter
            cur = s[right]
            if cur not in count:
                count[cur] = 1
            else:
                count[cur] += 1

            # find most freq letter
            max_freq = 0
            for _, freq in count.items():
                if freq > max_freq:
                    max_freq = freq

            window_len = right - left + 1

            # calc longest = window_len - count of most freq
            replace_count = window_len - max_freq

            # if replace_count > k: decrement/remove count[left], left += 1
            if replace_count > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
                continue

            if window_len > res:
                res = window_len

        return res

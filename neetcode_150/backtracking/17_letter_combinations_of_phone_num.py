from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        hmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []

        def dfs(i, comb):
            if len(comb) == len(digits):
                res.append(''.join(comb))
                return

            if i >= len(digits):
                return

            letters = hmap[digits[i]]
            for j in range(len(letters)):
                comb.append(letters[j])
                dfs(i + 1, comb)
                comb.pop()

        dfs(0, [])
        return res

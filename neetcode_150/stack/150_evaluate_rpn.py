import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.lstrip("-").isalnum():
                stack.append(int(t))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                res = 0
                if t == "+":
                    res = n1 + n2
                elif t == "-":
                    res = n2 - n1
                elif t == "*":
                    res = n1 * n2
                elif t == "/":
                    res = math.trunc(n2 / n1)

                stack.append(res)

        return stack[0]


s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))



class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        if len(s) == 0:
            return True

        st = []

        for p in s:
            if p in ['(', '{', '[']:
                st.append(p)
            else:
                if len(st) == 0:
                    return False
                peak = st[len(st) - 1]
                if (peak == '(' and p == ')' or
                        peak == '{' and p == '}' or
                        peak == '[' and p == ']'):
                    st.pop()
                else:
                    st.append(p)

        return len(st) == 0
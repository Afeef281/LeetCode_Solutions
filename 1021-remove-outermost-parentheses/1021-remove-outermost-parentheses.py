class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        count = 0
        result = ''

        for i in range(n):
            if s[i] == '(':
                if count > 0:
                    result += s[i]
                count += 1

            else:  # ')'
                count -= 1
                if count > 0:
                    result += s[i]

        return result
        
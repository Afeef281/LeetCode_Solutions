class Solution:
    def smallestPalindrome(self, s: str) -> str:
        strlist = list(s)
        n = len(strlist)
        half = strlist[:n//2]
        half.sort()
        if n ==1 or n ==3:
            return s

        elif n %2 != 0:
            string = "".join(half)
            string += str(s[n//2])
            for i in range(n//2-1,-1,-1):
                string += half[i]
        else:
            string = "".join(half)
            for i in range(n//2-1,-1,-1):
                string += str(half[i])
        return string

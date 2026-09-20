class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        sum =0

        for i in range(n):
            val = ord('z')-ord(s[i]) + 1
            sum += (val*(i+1))
        return sum
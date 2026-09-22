class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashstr ={}

        for ch in s:
            hashstr[ch] = hashstr.get(ch,0)+1

        for i in range(len(t)):
            if t[i] not in hashstr or hashstr[t[i]] == 0:
                return t[i]
            else:
                hashstr[t[i]] -= 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashstr = {}
        if len(s) != len(t):return False
        for char in s:
            if char not in hashstr:
                hashstr[char]=1
            else:
                hashstr[char] +=1
        for i in range(len(s)):
            if t[i] not in hashstr or hashstr[t[i]] == 0:
                return False
            else:
                hashstr[t[i]] -=1
                
        return True
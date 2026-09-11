class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashstr = {}
        if len(s) != len(t):return False
        for char in s:
            hashstr[char] = hashstr.get(char,0)+1
        for i in range(len(s)):
            if t[i] not in hashstr or hashstr[t[i]] == 0:
                return False
            else:
                hashstr[t[i]] -=1
                
        return True
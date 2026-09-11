class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashstr = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashstr:
                hashstr[s[i]]=1
            else:
                hashstr[s[i]] +=1
        for i in range(len(s)):
            if t[i] not in hashstr:
                return False
            elif hashstr[t[i]] == 0:
                return False
            else:
                hashstr[t[i]] -=1
                
        return True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashstr = {}
        for i in range(len(s)):
            if s[i] not in hashstr and t[i] not in hashstr.values():
                hashstr[s[i]] = t[i]
            else:
                if s[i] not in hashstr or hashstr[s[i]] != t[i] :
                    return False
        return True
        
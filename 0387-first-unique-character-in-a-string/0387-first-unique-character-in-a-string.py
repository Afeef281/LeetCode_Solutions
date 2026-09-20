class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashstr ={}
        n = len(s)

        for ch in s:
                hashstr[ch] = hashstr.get(ch,0)+1

        count =0
        for key,val in hashstr.items():
            if val == 1:
                ans = key
                break
            else:
                count +=1
        if count == len(hashstr):
            return -1
        for i in range(n):
            if s[i] == ans:
                return i 
            
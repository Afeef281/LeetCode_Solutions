class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count =0

        for i in range(n-1,-1,-1):
            if s[i] !=' ':
                count +=1
            elif s[i] == ' ' and count !=0:
                return count
            
            elif count == 0:
                continue
        return count
            
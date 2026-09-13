class Solution:
    def romanToInt(self, s: str) -> int:
        count =0
        n=len(s)
        roman ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        while i<n-1:
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                count += roman[s[i+1]]-1
                i+=1
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                count += roman[s[i+1]]-10
                i+=1
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                count += roman[s[i+1]]-100
                i+=1
            else:
                count += roman[s[i]]
            i+=1
        if i==n-1:
            count += roman[s[-1]]
        return count
            
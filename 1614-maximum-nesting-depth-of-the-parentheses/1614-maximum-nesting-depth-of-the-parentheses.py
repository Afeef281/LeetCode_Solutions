class Solution:
    def maxDepth(self, s: str) -> int:
        count =0
        nested =0
        for char in s:
            if char =='(':
                count +=1
            elif char ==')':
                count-=1
            nested =max(nested,count)
        return nested
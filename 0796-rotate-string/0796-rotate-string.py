class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        i=0
        while i<=n:
            if s == goal:
                return True
            else:
                arr = list(s)
                temp = arr[0]
                for j in range(n-1):
                    arr[j]=arr[j+1]
                arr[-1]= temp
                i+=1
                s="".join(arr)
        return False
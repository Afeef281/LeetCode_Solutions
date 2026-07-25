class Solution:
    def maxProduct(self, n: int) -> int:
        x=n
        count =0
        arr=[]
        max_pro = float('-inf')
        while x!= 0:
            arr.append(x %10)
            x = x//10
            count +=1
        for i in range(count-1):
            for j in range(i+1,count):
                m=arr[j]*arr[i]
                max_pro = max(max_pro,m)
        return max_pro

        
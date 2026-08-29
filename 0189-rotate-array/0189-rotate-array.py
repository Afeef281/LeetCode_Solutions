class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        
        k = k % n
        num =[]
        for i in range(n - k):
            num.append(nums[i]) 
        
        j = n - k
        
        for i in range(k):
            nums[i] = nums[j]
            j+=1
    
        j=0
        while j+k<n:
            nums[k+j] = num[j]
            j+=1
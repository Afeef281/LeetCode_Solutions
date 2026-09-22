class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        M ,m =0,0
        n =len(nums)
        res =float('-inf')
        for i in range(n):
            M = M + nums[i]
            res = max(res ,M)
            if M <0:
                M =0
            
        return res
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        M ,m =0,0
        n =len(nums)
        res =float('-inf')
        for i in range(n):
            # if M <0:
            #     M =0
            # if m < 0:
            #     m =0
            M = M + nums[i]
            # m = m + nums[n-i-1]

            res = max(res ,M)
            if M <0:
                M =0
            
        return res
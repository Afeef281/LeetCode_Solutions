class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        pro =1
        for i in range(len(nums)-3,len(nums)):
            pro = pro*nums[i]
        res = nums[0] * nums[1] * nums[-1]
        return max(res,pro)      
        
            
        
        
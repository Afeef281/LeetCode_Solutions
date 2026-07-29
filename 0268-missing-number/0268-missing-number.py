class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        if nums[0] == 0:
            for i in range(n-1):
                if nums[i] + 1 != nums[i+1]:
                    return nums[i]+1
        else:
            return 0

        return nums[n-1]+1
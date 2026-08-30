class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
    
        count = 0
        for i in nums:
            if i != 0:
                nums[count] = i
                count+=1

        while count < len(nums):
            nums[count] = 0
            count +=1
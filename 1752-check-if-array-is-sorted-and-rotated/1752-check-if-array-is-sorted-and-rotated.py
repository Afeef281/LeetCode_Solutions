class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                count +=1
        if nums[-1] > nums[0]:
            count +=1
        if count <2:
            return True
        else:
            return False


        
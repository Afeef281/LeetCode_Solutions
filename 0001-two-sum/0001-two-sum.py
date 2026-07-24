class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            first = num
            sec = target - first
            if sec in nums[i+1:]:
                return [i , nums[i+1:].index(sec) +(i+1)]
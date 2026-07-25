class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap ={}
        for n in range(len(nums)):
            if nums[n] in hashmap:
                return nums[n]
            hashmap[nums[n]] = n
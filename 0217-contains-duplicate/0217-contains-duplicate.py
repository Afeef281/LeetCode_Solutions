class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap ={}
        n = len(nums)

        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                return True
        return False
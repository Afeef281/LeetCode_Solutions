class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        hashmap = {}
        for i in range(n):
            if nums[i] in hashmap:
                hashmap[nums[i]]+= 1
            else:
                hashmap[nums[i]] =1
        res= 0
        nums_set =set(nums)
        for i in nums_set:
            res = max(res,hashmap[i])
        for key,val in hashmap.items():
            if res == val:
                return(key)
        
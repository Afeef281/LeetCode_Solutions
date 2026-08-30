class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # hashmap ={}
        # n = len(nums)

        # count =0
        # i=0
        # while i < n:
        #     if nums[i] == 1:
        #         count +=1
        #     else:
        #         hashmap[i] =count
        #         count =0
        #     i+=1
        # hashmap[i] =count
        # maxvalue =0
        # for value in hashmap.values():
        #     if value > maxvalue:
        #         maxvalue = value
        # return maxvalue

        res = 0
        count = 0

        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
            
            if res < count:
                res = count
        
        return res
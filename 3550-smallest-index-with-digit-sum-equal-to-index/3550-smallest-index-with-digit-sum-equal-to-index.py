class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] == i and nums[i]//10 == 0:
                return i
            val = nums[i]
            sum =0
            while val !=0:
                rem = val%10
                sum +=rem
                val = val//10
            if sum == i:
                return i
        return -1
            
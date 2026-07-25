class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)

        for n in nums_set:
            if (n-1) not in nums_set:
                length =1
                while n+length in nums_set:
                    length +=1
                ans = max(ans,length)
        return ans
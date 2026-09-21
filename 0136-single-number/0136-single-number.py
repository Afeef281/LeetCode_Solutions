class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in nums:
            if count[num] == 1:
                return num

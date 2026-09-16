class Solution:
    def hammingWeight(self, n: int) -> int:
        nums =[]
        x =n
        while x>0:
            nums.append(x%2)
            x = x //2
        nums.reverse()
        count =0
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
        return count
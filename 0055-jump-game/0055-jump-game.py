class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n =len(nums)
        jump = 0
        for i in range(n):
            if i>jump:
                return False
            jump = max(jump,i+nums[i])
        return True
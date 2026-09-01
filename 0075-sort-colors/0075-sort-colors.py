class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        x =0
        y=n-1
        
        i=0
        while x<= y:
            if nums[x] == 0:
                nums[x],nums[i] = nums[i],nums[x]
                i+=1
                x+=1
            elif nums[x] == 1:
                x+=1
            else:
                nums[x],nums[y] = nums[y],nums[x]
                y-=1

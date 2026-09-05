class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posi = []
        nega = []
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nega.append(nums[i])
            else:
                posi.append(nums[i])
        m=0
        p=0
        nums[0] = posi[p]
        p+=1
        
        for i in range(1,n):
            if i%2 ==0:
                nums[i] = posi[p]
                p+=1
            else:
                nums[i] = nega[m]
                m+=1
        return nums
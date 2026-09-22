class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max=cur_min=mini=maxi=total =0
        maxi=float('-inf')
        mini = float('inf')
        for num in nums:
           cur_max = max(num , cur_max + num)
           maxi = max(maxi, cur_max)

           cur_min = min(num , cur_min+ num)
           mini = min(mini , cur_min)
           total += num
        if mini == total:
            return maxi
        else:
            return max(maxi,total-mini)
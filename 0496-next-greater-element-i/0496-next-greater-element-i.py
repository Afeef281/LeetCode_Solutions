class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack =[]
        stack.append(nums2[-1])
        ans = [-1] *len(nums2)
        # hashmap={}
        hashmap = {x: -1 for x in nums2}
        for i in range(len(nums2)-1,-1,-1):
            # hashmap[nums2[i]]=hashmap.get(nums2[i],-1)
            while len(stack)!=0 and stack[-1]<=nums2[i]:
                stack.pop()
            if(len(stack)!=0):
                ans[i]=stack[-1]
                hashmap[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                nums1[i] = hashmap[nums1[i]]
        return nums1

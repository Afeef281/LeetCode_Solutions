# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        nums = []
        curr = head

        while curr:
            nums.append(curr.val)
            curr=curr.next

        n = len(nums)
        for i in range(n//2):
            if nums[i] != nums[-(i+1)]:
                return False
        return True
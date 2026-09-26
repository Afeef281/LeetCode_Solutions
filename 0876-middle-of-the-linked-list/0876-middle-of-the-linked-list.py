# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        curr = head
        count =0
        while curr != None:
            count+=1
            curr = curr.next
        for i in range(count//2):
            head = head.next
        return head
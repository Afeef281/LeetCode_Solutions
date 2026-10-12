# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count =0
        curr = head
        while curr!=None:
            count+=1
            curr = curr.next
        if count == n :
            return head.next
        curr = head
        
        for i in range(count-n-1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head

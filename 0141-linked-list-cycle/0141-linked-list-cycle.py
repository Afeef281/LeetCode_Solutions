# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashlink = {}
        curr = head

        while curr != None:
            if curr in hashlink:
                return True

            hashlink[curr] = 1
            curr = curr.next

        return False
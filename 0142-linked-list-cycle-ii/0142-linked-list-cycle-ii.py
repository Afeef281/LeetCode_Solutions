# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashlink = {}
        curr = head
        index = 0

        while curr != None:
            if curr in hashlink:
                return curr

            hashlink[curr] = index
            curr = curr.next
            index += 1

        return None

        
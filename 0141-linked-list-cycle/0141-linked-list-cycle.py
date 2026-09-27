# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hashlink = {}
        # pos =-1
        # curr = head
        # if head==None or head.next==None:
        #     return False

        # while curr!=None:
        #     if curr.val not in hashlink:
        #         pos+=1
        #         hashlink[curr.val] = pos
        #     elif hashlink[curr.val] != pos:
        #         return False
        #     curr = curr.next
        # return True

        hashlink = {}
        curr = head

        while curr != None:
            if curr in hashlink:
                return True

            hashlink[curr] = True
            curr = curr.next

        return False
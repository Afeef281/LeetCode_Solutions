# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        bits = []
        curr = head
        while curr!=None:
            bits.append(curr.val)
            curr=curr.next
        n = len(bits)
        for i in range(n//2):
            bits[i],bits[-(i+1)] = bits[-(i+1)],bits[i]
        res =0
        for i in range(n):
            if bits[i] == 1:
                res =res + (2**i)
        return res
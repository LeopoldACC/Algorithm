# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp = ListNode(-1)
        tmp.next = head
        l,f = tmp,head
        while n>0:
            f = f.next
            n-=1
        while f:
            l = l.next
            f = f.next
        l.next = l.next.next
        return tmp.next
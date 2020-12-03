# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:###
            return False
        l,f = head,head.next
        while l:
            if not f or not f.next:###
                return False
            l = l.next
            f = f.next.next
            if l==f:
                return True
        return False
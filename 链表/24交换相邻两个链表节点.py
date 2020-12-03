# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmp = ListNode(-1)
        tmp.next = head
        pre = tmp
        while head and head.next:
            ne = head.next
            head.next = head.next.next
            ne.next = head
            pre.next = ne
            pre = head
            head = head.next
        return tmp.next
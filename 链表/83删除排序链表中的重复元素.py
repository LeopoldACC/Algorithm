class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = ListNode(1e9+7)
        tmp.next = head
        p = head
        pre = tmp
        while p:
            while p and p.val == pre.val:
                p = p.next
            pre.next = p
            if not p:
                break
            pre = p
            p = p.next

        return tmp.next

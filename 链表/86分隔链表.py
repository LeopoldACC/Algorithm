class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        tmpl = ListNode(0)
        tmpr = ListNode(0)
        p = head
        l = tmpl
        r = tmpr
        while p:
            if p.val<x:
                l.next = p
                l = l.next
            else:
                r.next = p
                r = r.next
                
            p = p.next
        r.next = None
        l.next = tmpr.next
        return tmpl.next
ls = [1,4,3,2,5,2]
head = ListNode(ls[0])
p = head
for i in range(1,len(ls)):
    p.next = ListNode(ls[i])
    p = p.next
so = Solution()
so.partition(head,3)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cnt = {}
        p = head

        while p:
            cnt[p.val] = cnt.get(p.val,0)+1
            p = p.next
        tmp = ListNode(0)
        tmp.next = head
        pre = tmp
        
        p = head

        while p:
            while p and cnt[p.val]>=2:
                p = p.next
            pre.next = p
            pre = p
            p = p.next
        return tmp.next

ls = [1,2,3,3,4,4,5]
head = ListNode(ls[0])
p = head
for i in range(1,len(ls)):
    p.next = ListNode(ls[i])
    p = p.next
so = Solution()
so.deleteDuplicates(head)
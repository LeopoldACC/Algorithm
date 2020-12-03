# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        tmp = ListNode(0)
        tmp.next = head
        tmp_o = ListNode(0)
        tmp_o.next = head.next
        p = head
        cnt = 1
        pre_j,pre_o = None,None
        while p:
            if cnt%2==1:
                if pre_j:
                    pre_j.next = p
                pre_j = p
                print(pre_j.val)
            else:
                if pre_o:
                    pre_o.next = p
                pre_o = p
                
                
            cnt+=1
            ne = p.next
            if cnt%2==0:
                if not p.next:
                    p.next = None
                elif not p.next.next:
                    p.next = None
            p = ne
        pre_j.next = tmp_o.next
        return tmp.next
ls = [1,2,3,4,5]
head = ListNode(ls[0])
p = head
for i in range(1,len(ls)):
    p.next = ListNode(ls[i])
    p = p.next
so = Solution()
so.oddEvenList(head)
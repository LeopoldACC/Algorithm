# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        tmp = ListNode(-1)
        tmp.next = head
        f,l,m = tmp,tmp,tmp
        flag =False 
        while f and f.next:
            f = f.next.next
            l = l.next
            if l==f:
                flag = True
                break
        if not flag:
            return None
        while m!=l:
            m = m.next
            l = l.next
        return l
        # a + b + n*(c+b) = 2*(a+b)
        # n*c+n*b = a + b
        # n*c+(n-1)*b = a
        # (n-1)*(b+c) + c = a 创建第三个节点 从头节点走a步  等式左边则是在环内走(n-1)*(b+c)步

ls =[3,2,0,-4]
nodels = [ListNode(ls[i]) for i in range(len(ls))]
pos = 1
for i in range(1,len(ls)):
    nodels[i-1].next = nodels[i]
nodels[-1].next = nodels[pos]

so = Solution()
so.detectCycle(nodels[0])


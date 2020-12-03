class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        tmp = ListNode(0)
        tmp.next = head
        pre = tmp
        cur = head
        while cur:
            ne = cur.next
            p = tmp.next
            pre = tmp
            if not ne:
                break
            if ne.val<cur.val:
                nee = ne.next
                ne.next = None
                while p.next!=ne and p.val<ne.val:
                    p = p.next
                    pre = pre.next
                cur.next = nee#把ne删了
                pre.next = ne
                ne.next = p
            else:
                cur = cur.next
                continue
            if cur.next and cur.next.val>cur.val:
                cur = cur.next
        return tmp.next
nums = [-1,5,3,4,0]
dummy = ListNode(0)
cur = dummy
for num in nums:
    cur.next = ListNode(num)
    cur = cur.next
ls = dummy.next
s = Solution()
s.insertionSortList(ls)

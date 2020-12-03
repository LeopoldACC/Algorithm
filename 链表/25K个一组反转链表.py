# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            # tail走k步到当前段的终点
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            # ne 下一段的起点
            ne = tail.next
            # prev 下一段的起点 在k个序倒过来之后 p会指向下一段的起点
            prev = tail.next
            # p 这一段的起点 
            p = head
            while prev!=tail:
                nex = p.next#把p的下一个点及之后的链存下来
                p.next = prev #prev首先初始为下一段的起点
                prev = p#之后才是当前点
                p = nex#p移动到之前存的下一个点
            # 此时 tail = 2 -> head = 1 所以把变量名换一下
            head,tail = tail,head
            # pre接当前段head  | tail 接下一段nex | 更新下一段pre为当前段tail  | 更新下一段head为当前段tail.next
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next

            
nums = [1,2,3,4,5]
k=2
dummy = ListNode(0)
cur = dummy
for num in nums:
    cur.next = ListNode(num)
    cur = cur.next
ls = dummy.next
s = Solution()
s.reverseKGroup(ls,k)

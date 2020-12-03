# https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        l,f = head,head##这里f要初始化为head，不然在第二步中l和f永远碰不到
        while True:
            if not f or not f.next:
                return None
            l = l.next
            f = f.next.next
            if l==f:
                break
        f = head
        while f != l:
            f, l = f.next, l.next
        return f
            
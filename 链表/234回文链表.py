class ListNode():
    def __init__(self,val = None):
        self.val = val
        self.next = None

class Solution:
    def isPalindrome(self, head) -> bool:
        tmp = ListNode(0)
        tmp.next = head
        l,f = tmp,tmp
        while f and f.next:
            l = l.next
            f = f.next.next
        cur = l.next
        
        l.next = None
        prev = l
        while cur:
            ne = cur.next
            cur.next = prev
            prev = cur
            cur = ne
        left,right = head,prev
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

def create_Linked_list(ls):
    if not ls:
        return None
    tmp = ListNode(0)
    pre=tmp
    i=0
    while i<len(ls):
        head = ListNode(ls[i])
        pre.next = head
        pre = head
        i+=1
    return tmp.next

ls = [1,0,1]
head = create_Linked_list(ls)
s = Solution()
s.isPalindrome(head)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nodels = []
        while head:
            nodels.append(head.val)
            head = head.next
        def dfs(l,r):
            if l>r:
                return None
            mid = (l+r)//2
            root = TreeNode(nodels[mid])
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root
        return dfs(0,len(nodels)-1)
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def dfs(head):
            if not head:
                return None
            if not head.next:
                return TreeNode(head.val)
            mid,f = head,head
            while f and f.next:
                pre = mid
                mid = mid.next
                f = f.next.next
            pre.next = None
            root = TreeNode(mid.val)
            root.left = dfs(head)
            root.right = dfs(mid.next)
            return root
        return dfs(head)

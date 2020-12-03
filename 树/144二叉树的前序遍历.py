# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return None
        res = []
        stk = []
        p = root
        while stk or p:
            while p:
                res.append(p.val)
                stk.append(p)
                p = p.left
            p = stk.pop()
            p = p.right
        return res
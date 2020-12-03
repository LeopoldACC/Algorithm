# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(t1,t2):
            if not t1 and not t2:
                return None
            if t1 and not t2:
                return t1
            if not t1 and t2:
                return t2
            t2.val+=t1.val
            t2.left = dfs(t1.left,t2.left)
            t2.right = dfs(t1.right,t2.right)
            return t2
        return dfs(t1,t2)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node,d):
            if not node:
                return d-1
            l_d = dfs(node.left,d+1)
            r_d = dfs(node.right,d+1)
            return max(l_d,r_d)
        return dfs(root,1)
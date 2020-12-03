# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.pre = -float('inf')
        self.res = float('inf')
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res = min(self.res,abs(root.val-self.pre))
            self.pre = root.val
            dfs(root.right)
        dfs(root)
        return self.res
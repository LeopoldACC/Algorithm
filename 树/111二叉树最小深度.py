class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root,d):
            if not root:
                return 1e4
            if not root.left and not root.right:
                return d
            return min(dfs(root.left,d+1),dfs(root.right,d+1))
        return dfs(root,1)
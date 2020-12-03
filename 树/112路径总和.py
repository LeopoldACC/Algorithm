class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        def dfs(root,sums):
            if not root:
                return False
            if not root.left and not root.right:
                return sums+root.val==target
            return dfs(root.left,sums+root.val) or dfs(root.right,sums+root.val)
        return dfs(root,0)
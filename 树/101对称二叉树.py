class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(p,q):
            if not p and q or not q and p:
                return False
            if not p and not q:
                return True
            return dfs(p.right,q.left) and dfs(p.left,q.right) and p.val == q.val
            
        return dfs(root,root)
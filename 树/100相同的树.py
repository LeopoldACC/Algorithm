# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if (not p and q) or (not q and p):
            return False
        if not p and not q:
            return True
        l_eq = self.isSameTree(p.left,q.left)
        r_eq = self.isSameTree(p.right,q.right)

        return p.val==q.val and l_eq and r_eq

root1 = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(3)
root1.left = l1
root1.right = r1

root2 = TreeNode(1)
l2 = TreeNode(2)
r2 = TreeNode(3)
root2.left = l2
root2.right = r2

s = Solution()
s.isSameTree(root1,root2)
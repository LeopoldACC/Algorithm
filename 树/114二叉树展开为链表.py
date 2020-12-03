# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ls = []
        def firstorder(n):
            if not n:
                return
            ls.append(n)
            firstorder(n.left)
            firstorder(n.right)
        firstorder(root)
        for i in range(1,len(ls)):
            prev,cur = ls[i-1],ls[i]
            prev.left = None
            prev.right = cur
            
tree = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(5)
tree.left = l1
tree.right = r1
l11 = TreeNode(3)
r11 = TreeNode(4)
r21 = TreeNode(6)
l1.left = l11
l1.right = r11
r1.right = r21

s = Solution()
s.flatten(tree)
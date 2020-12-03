# Definition for a binary tree node.
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/tu-jie-gou-zao-er-cha-shu-wei-wan-dai-xu-by-user72/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        def dfs(inorder,postorder):
            if not inorder:
                return None
            root = TreeNode(postorder[-1])
            r_i = inorder.index(root.val)
            root.left = dfs(inorder[:r_i],postorder[:r_i])
            root.right = dfs(inorder[r_i+1:],postorder[r_i:-1])
            return root
        return dfs(inorder,postorder)
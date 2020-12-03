# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        # if not root:
        #     return None
        # self.sums = 0
        # def dfs(root):
        #     if not root:
        #         return 
        #     dfs(root.right)
        #     root.val+=self.sums
        #     self.sums=root.val
        #     dfs(root.left)
        # dfs(root)
        # return root
        stk = []
        sums = 0
        p = root
        while p or len(stk)>0:
            while p:
                stk.append(p)
                p = p.right
            p = stk.pop()
            p.val+=sums
            sums = p.val
            p = p.left#不用先判断有没有root.left
        return root
            

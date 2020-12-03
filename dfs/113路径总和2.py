# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res=[]
        def dfs(root,path,t):
            if not root:
                return
            if t==root.val and not root.left and not root.right:
                res.append(path[:]+[root.val])
                return
            
            path.append(root.val)
            dfs(root.left,path,t-root.val)
            path.pop()

            path.append(root.val)
            dfs(root.right,path,t-root.val)
            path.pop()
        dfs(root,[],sum)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxi = -float('inf')
        def dfs(node):
            if not node:###空指针情况返回0
                return 0
            left = max(dfs(node.left),0)###如果左子树最大值<0，舍弃左子树
            right = max(dfs(node.right),0)###如果右子树最大值<0，舍弃右子树

            self.maxi = max(self.maxi,node.val+left+right)

            return node.val+max(left,right)###到叶子结点就返回叶子节点的值
        dfs(root)
        return self.maxi
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 状态表示 
# f[] 当前节点偷 当前
# 卡在哪？ 状态计算  
# 当前节点偷 则两个子节点不能偷 
# 当前节点不偷 则两个子节点偷或不偷都可以
# 所以 要dfs到底把 子节点偷 和 不偷的价值都计算出来
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(node):
            if not node:
                return 0,0#左边不偷 右边偷
            ln,ly = dp(node.left)
            rn,ry = dp(node.right)
            return max(ln,ly)+max(rn,ry),node.val+ln+rn
        return max(dp(root))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def dfs(pre,post):
            if not pre:
                return None
            root = TreeNode(pre[0])
            if len(pre)==1:
                return root
            l_cnt = post.index(pre[1])+1
            # 前序 根 左 右 pre[1] == 左子树根节点  又后序中为[左右(左根)] [左右(右根)] 根 则我们只需再post中找到 pre[1]的index+1 即找到 左子树的结点数
            root.left = dfs(pre[1:1+l_cnt],post[:l_cnt])
            root.right = dfs(pre[1+l_cnt:],post[l_cnt:-1])
            return root
        return dfs(pre,post)
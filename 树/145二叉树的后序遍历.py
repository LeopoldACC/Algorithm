# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        res,stk = [],[]
        p = root
        prev = None
        while p or stk:
            while p:
                stk.append(p)
                p=p.left
            p = stk.pop()
            if not p.right or p.right == prev:#左右(没有右了)中 左右中(从右上来了)
                res.append(p.val)
                prev = p
                p = None
            else:
                stk.append(p)
                p = p.right
        return res

# 二刷
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stk = []
        p = root
        pre = None
        while p or stk:
            while p:
                stk.append(p)
                p = p.left
            p = stk.pop()
            
            if not p.right or p.right==pre:
                res.append(p.val)
                pre = p
                p = None#p如果不赋成None会导致while p or stk:这句话死循环
            else:
                stk.append(p)
                p = p.right

        return res
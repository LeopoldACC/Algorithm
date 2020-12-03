class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:#递归
    def inorder(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder_list = []
        def get_inorder(node):
            if not node:
                return
            get_inorder(node.left)
            inorder.append(node)
            get_inorder(node.right)
        get_inorder(root)
        return inorder_list

class Solution:#栈
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        # 用p当做指针
        p = root
        while p or stack:
            # 把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            # 输出 栈顶元素
            p = stack.pop()
            res.append(p.val)
            # 看右子树
            p = p.right
        return res


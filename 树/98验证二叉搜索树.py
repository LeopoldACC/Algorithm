class Solution0:###自己写的有问题，为什么，因为只考虑了连续两层的关系，而更深的大小关系就不能确保了
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        l = self.isValidBST(root.left)
        r = self.isValidBST(root.right)
        if root.left:
            if root.left.val>=root.val:
                return False
        if root.right:
            if root.right.val<=root.val:
                return False
        return l and r

class Solution:#传父节点值
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root,-float('inf'),float('inf'))

    def dfs(self,root,low=-float('inf'),up=float('inf')):
        if not root:
            return True
        
        if root.val <=low or root.val >=up:### <= 等于的情况也不允许
            return False
        l = self.dfs(root.left,low,root.val)
        r = self.dfs(root.right,root.val,up)

        return l and r
class Solution:#中序遍历 stack尾节点维护pre.val
    def isValidBST(self, root: TreeNode) -> bool:
        stack,pre = [],-float('inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val <=pre:
                return False
            pre = root.val
            root = root.right
        return True
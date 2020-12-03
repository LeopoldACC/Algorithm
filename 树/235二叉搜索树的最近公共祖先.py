# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        fa_p = set()
        fa_p.add(p)
        def dfs_p(root):
            if not root:
                return False
            if root==p:
                return True
            l = dfs_p(root.left)
            r = dfs_p(root.right)
            if l or r:
                fa_p.add(root)
                return True
            return False
        dfs_p(root)
        self.max_d = -1
        self.res = None
        def dfs_q(root,d):
            if not root:
                return False
            if root==q:
                if d>self.max_d and root in fa_p:
                    self.max_d = d
                    self.res = q
                return True
            l = dfs_q(root.left,d+1)
            r = dfs_q(root.right,d+1)
            if l or r:
                if d>self.max_d and root in fa_p:
                    self.max_d = d
                    self.res = root
                return True
            return False
        dfs_q(root,0)
        return self.res
    
# root = TreeNode(6)
# l1 = TreeNode(2)
# r1 = TreeNode(8)
# root.left = l1
# root.right = r1
# l11 =TreeNode(0)
# l12 = TreeNode(4)
# l1.left = l11
# l1.right = l12

# r11 = TreeNode(7)
# r12 = TreeNode(9)
# r1.left = r11
# r1.right = r12
ls = [3,1,4,None,2]
ls = [TreeNode(x) for x in ls if x!=None]
ls[0].left = ls[1]
ls[0].right = ls[2]
ls[1].right = ls[3]

root = ls[0]
p = ls[3]
q = ls[0]
so = Solution()
so.lowestCommonAncestor(root,p,q)
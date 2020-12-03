# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
     i
   s1 s2
f[i][0] 节点i被父节点看到的所有方案 则s1和s2要么被子节点看到1 要么放摄像头2 Σmin(f[s1][1],f[s1][2])
f[i][1] 节点i被子节点看到的所有方案 则从s1和s2中选一个最小的min(f[s1][2],f[s2][2])+min(f[s另一个][2],f[s另一个][1])
f[i][2] 节点i上放摄像头的所有方案   则f[s1][0]+f[s2][0]
如果s1为空 则f[s1][0]=f[s1][1]=f[s1][2]=0
'''
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        f = self.dfs(root)
        return min(f[1],f[2])#根节点没有父节点
    def dfs(self,u):
        f = [0,0,float('inf')]
        if not u:#如果节点s1为空  则s1[2]=无穷 来让 s1[2]+min(s2[2],s2[1]) s1放摄像头+min(s2放,s2被i看到)的方案不被选
            return f
        s1 = self.dfs(u.left)
        s2 = self.dfs(u.right)
        f[0] = min(s1[1],s1[2])+min(s2[1],s2[2])
        f[1] += min(s1[2]+min(s2[2],s2[1]),s2[2]+min(s1[2],s1[1]))#s2放摄像头+min(s1放,s1被i看到)
        f[2] = 1
        f[2] += min(s1[0],s1[1],s1[2])+min(s2[0],s2[1],s2[2])
        return f 
s = Solution()
root = TreeNode(0)
l1 = TreeNode(0)
l2 = TreeNode(0)
r2 = TreeNode(0)

root.left = l1
l1.left = l2
l1.right = r2
s.minCameraCover(root)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#空间 O(n)
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        cnt = {}
        self.maxi = -float('inf')
        def dfs(root):
            if not root:
                return 
            cnt[root.val] = cnt.get(root.val,0)+1
            self.maxi = max(self.maxi,cnt[root.val])
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res = []
        for x in cnt:
            if cnt[x] == self.maxi:
                res.append(x)
        return res
#空间O(1)
class Solution:
    def findMode(self, root: TreeNode):
        self.cnt = 1
        self.maxi = -float('inf')
        self.pre = -float('inf')
        self.res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if root.val == self.pre:
                self.cnt+=1
            else:
                self.cnt =1
            if self.cnt == self.maxi:
                self.res.append(root.val)
            if self.cnt > self.maxi:
                self.res = [root.val]
                self.maxi = self.cnt
            self.pre = root.val
            dfs(root.right)
        dfs(root)
        return self.res
so = Solution()
root = TreeNode(1)
r1 = TreeNode(2)
r2 = TreeNode(2)
root.right = r1
r1.left = r2
so.findMode(root)
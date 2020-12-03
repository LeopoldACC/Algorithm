class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        def dfs(start,end):
            if start>end:
                return [None,]
            alls = []
            for i in range(start,end+1):
                lt = dfs(start,i-1)
                rt = dfs(i+1,end)
                for l in lt:
                    for r in rt:
                        curTree = TreeNode(i)
                        curTree.left = l
                        curTree.right = r
                        alls.append(curTree)
            return alls
        return dfs(1,n) if n else []
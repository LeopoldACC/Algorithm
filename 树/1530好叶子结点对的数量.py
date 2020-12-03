class Solution:
    def dfs(self, root, depth):
        if not root:
            return []
        if not root.left and not root.right:
            return [depth]
        l = self.dfs(root.left, depth + 1)#左叶子节点集合
        r = self.dfs(root.right, depth + 1)#右叶子节点集合
        ans = [i for i in itertools.chain(l, r) if i - depth < self.distance]#总叶子节点集合
        for i in l:#对左叶子节点的深度进行遍历
            if i - depth < self.distance:
                for j in r:#对右叶子节的深度进行遍历
                    if j + i - depth - depth <= self.dist ance:#i-depth为当前节点到左叶子节点距离 j-depth为当前节点到右叶子节点距离
                        self.ans += 1
        return ans

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        self.distance = distance
        self.dfs(root, 0)
        return self.ans
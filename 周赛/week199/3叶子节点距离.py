class Solution:
    def dfs(self, root, depth):
        if not root:
            return []
        if not root.left and not root.right:
            return [depth]
        l = self.dfs(root.left, depth + 1)
        r = self.dfs(root.right, depth + 1)
        ans = [i for i in itertools.chain(l, r) if i - depth < self.distance]
        for i in l:
            if i - depth < self.distance:
                for j in r:
                    if j + i - depth - depth <= self.distance:
                        self.ans += 1
        return ans

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        self.distance = distance
        self.dfs(root, 0)
        return self.ans
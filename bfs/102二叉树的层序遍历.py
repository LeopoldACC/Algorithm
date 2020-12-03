class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        import collections
        q = collections.deque([])
        res = []
        if not root:return res
        q.append(root)
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp[:])
        return res
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([])
        q.append(root)
        idx = 0
        res = []
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # print(tmp)
            if idx%2==0:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            idx+=1
            
        return res
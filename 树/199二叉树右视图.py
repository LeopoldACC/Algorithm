# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        q = collections.deque([])
        maxdepth = -1
        q.append((root,0))
        r_d = {}
        while q:
            node,depth = q.popleft()
            if node:
                maxdepth = max(maxdepth, depth)
                if depth not in r_d:
                    r_d[depth] = node.val
                q.append((node.right,depth+1))
                q.append((node.left,depth+1))
        return [r_d[depth] for depth in r_d]
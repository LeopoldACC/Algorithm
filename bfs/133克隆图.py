
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def bfs(self, node: 'Node') -> 'Node':
        if not node:
            return node
        q = collections.deque([node])
        visit = {}
        visit[node] = Node(node.val,[])
        while q:
            root = q.popleft()
            for ne in root.neighbors:
                if ne not in visit:
                    visit[ne] = Node(ne.val,[])
                    q.append(ne)
                visit[root].neighbors.append(visit[ne])
        return visit[node]
    def dfs(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visit = {}
        def dfs(root):
            if root in visit:
                return visit[root]
            visit[root] = Node(root.val,[])
            for ne in root.neighbors:
                visit[root].neighbors.append(dfs(ne))
            return visit[root]
        dfs(node)
        return visit[node]
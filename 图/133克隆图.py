class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        q = collections.deque([])
        q.append(node)
        vis = {}
        vis[node] = Node(node.val,[])
        while q:
            for _ in range(len(q)):
                t = q.popleft()
                for ne in t.neighbors:
                    if ne not in vis:
                        vis[ne] = Node(ne.val,[])
                        q.append(ne)
                    vis[t].neighbors.append(vis[ne])
        return vis[node]

# 错解--因为ne可能在之前已经被创建过 如果不用字典把之前创建过的ne会导致每次都创建新的
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        q = collections.deque([])
        q.append(node)
        vis = set()
        vis.add(node)
        newt = None
        while q:
            for _ in range(len(q)):
                t = q.popleft()
                if not newt:
                    newt = Node(t.val)
                    root = newt
                else:
                    newt = Node(t.val)
                for ne in t.neighbors:
                    if ne not in vis:
                        newne = Node(ne.val)
                        vis.add(ne)
                        q.append(ne)
                    newt.neighbors.append(newne)
        return root
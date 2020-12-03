class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = {x:0 for x in range(n)}
        edge = {x:[] for x in range(n)}
        for x,y in edges:
            degree[x]+=1
            degree[y]+=1
            edge[x].append(y)
            edge[y].append(x)
        q = collections.deque([])
        vis = set()
        for i in range(n):
            if degree[i]==1:
                q.append(i)
                vis.add(i)
        res = [0]
        while q:
            res = [x for x in q]
            for _ in range(len(q)):
                node = q.popleft()
                for ne in edge[node]:
                    if ne not in vis:
                        degree[ne]-=1
                        if degree[ne]==1:
                            q.append(ne)                        
                            vis.add(ne)
        return res
s =Solution()
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
s.findMinHeightTrees(n,edges)
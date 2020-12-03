import collections
class Solution:
    def maxProbability(self, n: int, edges, P, start: int, end: int) -> float:
        pre = {i:[] for i in range(n)}
        
        for i,edge in enumerate(edges):
            pre[edge[0]].append((edge[1],P[i]))
            pre[edge[1]].append((edge[0],P[i]))
        visit = set()
        res = float('inf')
        q = collections.deque([(start,1)])
        while q:
            node,p = q.pop()
            visit.add(node)
            if node == end:
                res = min(res,p)
            for neb in pre[node]:
                if neb not in visit:
                    q.append((neb[0],neb[1]*p))
        return res if res!=0.0 else 0.0    

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        G = [{} for _ in xrange(n)]
        for (i,j), p in zip(edges, succProb):
            G[i][j] = G[j][i] = p
            
        heap = [[-1.0, start]]
        dp = [0.0] * n
        while heap:
            p, i = heapq.heappop(heap)
            p = -p
            if i == end: return p
            if p < dp[i]: continue
            dp[i] = p
            for j in G[i]:
                if p * G[i][j] > dp[j]: 
                    heapq.heappush(heap, [-p * G[i][j], j])
                    dp[j] = -p * G[i][j]
        return 0.0
            
n=3
edges = [[0,1],[1,2],[0,2]]
p =[0.5,0.5,0.2]
start = 0
end = 2
so = Solution()
so.maxProbability(n,edges,p,start,end)    
        
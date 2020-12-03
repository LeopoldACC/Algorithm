import collections
class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        pre = {i:0 for i in range(n)}
        neigh = {i:[] for i in range(n)}
        for fa,son in edges:
            pre[fa]+=1
            neigh[son].append(fa)
        cnt = {i:[0]*26 for i in range(n)}
        for i in cnt:
            cnt[i][ord(labels[i])-ord('a')]=1
        res = [0]*n
        q = collections.deque([])
        for i in pre:
            if pre[i]==0:
                q.append(i)
                res[i]=1
        
        while q:
            node = q.pop()
            for i in neigh[node]:
                for j in range(26):
                    cnt[i][j]+=cnt[node][j]
                pre[i]-=1
                if pre[i]==0:
                    q.append(i)
                    res[i] = cnt[i][ord(labels[i])-ord('a')]
            
        return res
class Solution1:
    def countSubTrees(self, n: int, edges, labels: str):
        pre = {i:0 for i in range(n)}
        neigh = {i:[] for i in range(n)}
        visited = {i:False for i in range(n)}
        for fa,son in edges:
            pre[fa]+=1
            pre[son]+=1
            neigh[son].append(fa)
            neigh[fa].append(son)
        cnt = {i:[0]*26 for i in range(n)}
        for i in cnt:
            cnt[i][ord(labels[i])-ord('a')]=1
        res = [0]*n
        q = collections.deque([])
        for i in pre:
            if pre[i]==1:
                q.append(i)
                res[i]=1
        
        while q:
            node = q.popleft()
            visited[node] =True
            for i in neigh[node]:
                if visited[i]:
                    continue
                for j in range(26):
                    cnt[i][j]+=cnt[node][j]
                pre[i]-=1
                if pre[i]==0 or pre[i]==1:
                    q.append(i)
                    res[i] = cnt[i][ord(labels[i])-ord('a')]
            
        return res
s = Solution1()
n = 4
edges = [[0,2],[0,3],[1,2]]
labels = "aeed"
edges =[[0,1],[1,2],[0,3]]
labels ="bbbb"

n = 7
edges =[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels ="abaedcd"
n =6
edges =[[0,1],[0,2],[1,3],[3,4],[4,5]]
labels ="cbabaa"
ans = s.countSubTrees(n,edges,labels)
print(ans)
class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix:return 0###在之前的深搜过程中就已经搜过了
        m,n = len(matrix),len(matrix[0])
        
        memo = [[0] * n for _ in range(m)]
        def dfs(x,y):
            if memo[x][y]!=0:
                return memo[x][y]###不能return空
            memo[x][y] += 1
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = x+dx,y+dy###y+dy写成了x+dy
                if 0<=nx<m and 0<=ny<n and matrix[nx][ny]>matrix[x][y]:
                    memo[x][y] = max(memo[x][y],dfs(nx,ny)+1)
            return memo[x][y]
        res = 0
        
        for i in range(m):
            for j in range(n):
                res = max(res,dfs(i,j))
        return res

#topo_sort

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:return 0
        m,n = len(matrix),len(matrix[0])
        out_d = [[0]*n for _ in range(m)]
        #出度->当前值比邻域值小 当前值往邻域点走
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        q = collections.deque([])
        for x in range(m):
            for y in range(n):
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and matrix[nx][ny]>matrix[x][y]:
                        out_d[x][y] +=1
                if out_d[x][y] == 0:
                    q.append((x,y))
        res = 0
        #基于出度 -> bfs总层数就是最长递增长度
        while q:
            res += 1
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and matrix[nx][ny]<matrix[x][y]:
                        out_d[nx][ny]-=1
                        if out_d[nx][ny]==0:
                            q.append((nx,ny))
        
        return res


class Solution0:
    def minimumEffortPath(self, h) -> int:
        m,n = len(h),len(h[0])
        f = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                f[i][j] = min(max(f[i-1][j],abs(h[i][j]-h[i-1][j])),max(f[i][j-1],abs(h[i][j]-h[i][j-1]))) 
        
        return f[m-1][n-1]
import heapq
class Solution:
    def minimumEffortPath(self, h) -> int:
        m,n = len(h),len(h[0])
        f = [[float('inf')]*n for _ in range(m)]
        st = [[False]*n for _ in range(m)]
        f[0][0] = 0
        q = []
        heapq.heappush(q,(0,0,0))
        while q:
            z,x,y = heapq.heappop(q)
            if st[x][y]:
                continue
            st[x][y] = True
            f[x][y] = z
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and not st[nx][ny]:
                    heapq.heappush(q,(max(z,abs(h[nx][ny]-h[x][y])),nx,ny))
                    
        return f[m-1][n-1]
h = [[1,2,2],[3,8,2],[5,3,5]]
s = Solution()
s.minimumEffortPath(h)
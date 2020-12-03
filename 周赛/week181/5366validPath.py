class Solution:
    def hasValidPath(self, grid):
        
        dir = {1:[(0,1),(0,-1)],
               2:[(1,0),(-1,0)],
               3:[(1,0),(0,-1)],
               4:[(0,1),(1,0)],
               5:[(0,-1),(-1,0)],
               6:[(0,1),(-1,0)]}
        
        x,y = 0,0
        m,n = len(grid),len(grid[0])
        if x==m-1 and y==n-1:
            return True
        from collections import deque
        queue = deque([(x,y)])
        while queue:
            x,y = queue.popleft()
            for dx,dy in dir[grid[x][y]]:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]!=-1:
                    for ndx,ndy in dir[grid[nx][ny]]:
                        if ndx+dx==0 and ndy+dy==0:
                            if nx==m-1 and ny==n-1:
                                return True
                            queue.append((nx,ny))
            grid[x][y]=-1
        return False
s =Solution()
grid = [[1,1,1,1,1,1,1,3]]
grid =[[1,1,2]]
print(s.hasValidPath(grid))
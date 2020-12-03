class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        m,n = len(board),len(board[0])
        f = {}
        def find(x):
            # f.setdefault(x, x)
            f[x] = f.get(x,x)
            if f[x]!=x:
                f[x] = find(f[x])
            return f[x]
        dummy = -1
        def union(x,y):
            f[find(y)] = find(x)
        for x in range(m):
            for y in range(n):
                if board[x][y]=='O':
                    if x==0 or x==m-1 or y==0 or y==n-1:
                        union(x*n+y,dummy)
                    else:
                        for dx,dy in dirs:
                            nx,ny = x+dx,y+dy 
                            if 0<=nx<m and 0<=ny<n and board[nx][ny]=='O':
                                union(x*n+y,nx*n+ny)

        for x in range(m):
            for y in range(n):
                if find(dummy) == find(x*n+y):
                    board[x][y] = 'O'
                else:
                    board[x][y] = 'X'
        
        
        

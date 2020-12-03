class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        cx,cy = click[0],click[1]
        m,n = len(board),len(board[0])
        if board[cx][cy]=='M':
            board[cx][cy] = 'X'
            return board
        if board[cx][cy]!='E':
            return board
        visit = [[False] * n for _ in range(m)]
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]
        def dfs(x,y):
            visit[x][y] = True
            cnt = 0
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and board[nx][ny]=='M':
                    cnt+=1
            if cnt>0:
                board[x][y]=str(cnt)
            else:
                board[x][y] = 'B' 
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and board[nx][ny]=='E' and not visit[nx][ny]:
                        visit[nx][ny] = True
                        dfs(nx,ny)
        dfs(cx,cy)
        return board
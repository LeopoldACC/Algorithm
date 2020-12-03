class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(x,y):
            board[x][y]='#'
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy 
                if 0<=nx<m and 0<=ny<n and board[nx][ny]=='O':
                    dfs(nx,ny)
        
        m,n = len(board),len(board[0])
        for i in range(n):
            if board[0][i] == 'O':
                board[0][i]='#'
                dfs(0,i)
            if board[m-1][i] == 'O':
                board[m-1][i]='#'
                dfs(m-1,i)       
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] ='#'
                dfs(i,0)
            if board[i][n-1]=='O':
                board[i][n-1]='#'
                dfs(i,n-1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
        

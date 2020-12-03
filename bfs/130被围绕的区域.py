import collections
class Solution0:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        m,n = len(board),len(board[0])
        visit = set()
        
        def bfs():
            q = collections.deque([])
            for i in range(n):
                if board[0][i]=='O':
                    q.append((0,i))
                if board[m-1][i] =='O':
                    q.append((m-1,i))
            for i in range(m):
                if board[i][0]=='O':
                    q.append((i,0))
                if board[i][n-1]=='O':
                    q.append((i,n-1))
            while q:
                x,y = q.popleft()
                board[x][y] = '#'
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy 
                    if 0<=nx<m and 0<=ny<n and board[nx][ny]=='O':
                        q.append((nx,ny))
        bfs()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j]=='#':
                    board[i][j] = 'O'
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        q = collections.deque([])
        m,n = len(board),len(board[0])
        st = [[False]*n for _ in range(m)]
        def bfs(i,j):
            q.append([i,j])
            st[i][j] = True
            cor = []
            f = True
            while q:
                for _ in range(len(q)):
                    x,y = q.popleft()
                    cor.append([x,y])
                    if x==0 or x==m-1 or y==0 or y==n-1:
                        f = False
                        # break
                    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                        nx,ny = x+dx,y+dy 
                        if nx<0 or nx>m-1 or ny<0 or ny>n-1 or st[nx][ny] or board[nx][ny]=='X':
                            continue
                        q.append([nx,ny])
                        st[nx][ny] = True
            if f:
                for x,y in cor:
                    board[x][y] = 'X'
        for i in range(m):
            for j in range(n):
                
                if board[i][j]=='O' and not st[i][j]:
                    bfs(i,j)                                    
        
s = Solution()
b = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
s.solve(b)
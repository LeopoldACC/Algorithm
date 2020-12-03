class Solution2:#wrong ans
    def exist(self, board, word: str) -> bool:
        m,n = len(board),len(board[0])
        vis = set()
        def dfs(i,x,y):
            if i == len(word)-1:
                return True
            tmp = False
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx = x+dx
                ny = y+dy
                if 0<=nx<m and 0<=ny<n and i+1<len(word) and board[nx][ny]==word[i+1]:
                    vis.add(nx*n+ny)
                    tmp |= dfs(i+1,nx,ny)
                    vis.remove(nx*n+ny)
            return tmp
        s = word[0]
        
        res = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == s:
                    vis.add(i*n+j)
                    res |= dfs(0,i,j)
                    vis.remove(i*n+j)
        return res
class Solution1:#right ans
    def exist(self, board, word: str) -> bool:
        m,n = len(board),len(board[0])
        vis = set()
        def dfs(i,x,y):
            if i == len(word)-1:
                return True
            tmp = False
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx = x+dx
                ny = y+dy
                if 0<=nx<m and 0<=ny<n and i+1<len(word) and board[nx][ny]==word[i+1] and nx*n+ny not in vis:
                    vis.add(nx*n+ny)
                    if dfs(i+1,nx,ny):
                        tmp = True#搜到一个结果就直接break 没必要|
                        break
                    vis.remove(nx*n+ny)
            return tmp
        s = word[0]
        
        res = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == s:
                    vis.add(i*n+j)
                    res |= dfs(0,i,j)
                    vis.remove(i*n+j)
        return res
class Solution:
    def exist(self, board, word: str) -> bool:
        m,n = len(board),len(board[0])
        st = [[False] * n for _ in range(m)]
        self.res = False
        def dfs(x,y,idx):
            if idx == len(word):
                self.res = True
                return True
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and not st[nx][ny]:
                    if board[nx][ny] == word[idx]:
                        st[nx][ny] = True
                        if dfs(nx,ny,idx+1):
                            return True
                        st[nx][ny] = False

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    st[i][j] = True
                    if dfs(i,j,1):
                        return True 
                    st[i][j] = False
        return self.res
s = Solution()
board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
s.exist(board,word)
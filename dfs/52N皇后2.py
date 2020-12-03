class Solution:
    def totalNQueens(self, n: int) -> int:
        dig = [False] * 2 * n
        udig = [False] * 2 * n
        cols = [False] * n
        # res = []
        self.res = 0
        def dfs(row,path):
            if row==n and len(path)==n:
                # board = []
                # string = "."*n
                # for col in path:
                #     board.append(string[:col]+"Q"+string[col+1:])
                # res.append(board)
                self.res += 1
                return

            for col in range(n):
                if cols[col] or dig[n+col-row] or udig[row+col]:
                    continue
                cols[col],dig[n+col-row],udig[row+col] = True,True,True
                dfs(row+1,path+[col])
                cols[col],dig[n+col-row],udig[row+col] = False,False,False
        dfs(0,[])
        return self.res
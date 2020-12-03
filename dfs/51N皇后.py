class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def get_board():
            b = [['.']*n for _ in range(n)]
            for row in range(len(board)):
                for col in range(n):
                    if col == board[row]:
                        b[row][col] = 'Q'
            ans = []
            for row in range(len(b)):
                ans.append(''.join(b[row]))
            return ans

        def dfs(row):
            if row==n:
                path = get_board()
                res.append(path)
            for col in range(n):
                if col in cols or row-col in dig or row+col in udig:
                    continue
                cols.add(col)
                board[row] = col
                dig.add(row-col)
                udig.add(row+col)
                dfs(row+1)
                cols.remove(col)
                dig.remove(row-col)
                udig.remove(row+col)
        res = []
        board = [-1] * n
        cols = set()
        dig = set()
        udig = set()
        dfs(0)
        return res
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def od(ch):
            return ord(ch)-ord('1')
        
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        recs = [[False] * 9 for _ in range(9)]
        void = []
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    rows[i][od(board[i][j])] = True
                    cols[j][od(board[i][j])] = True
                    recs[i//3*3+j//3][od(board[i][j])] = True
                else:
                    void.append([i,j])
        # print(void)

        def dfs(idx):
            if idx == len(void):
                return True
            i = void[idx][0]
            j = void[idx][1]
            for k in range(1,10):
                num = str(k)
                if not rows[i][od(num)] and not cols[j][od(num)] and not recs[i//3*3+j//3][od(num)]:
                    board[i][j] = num###先赋值 再作od()
                    rows[i][od(board[i][j])] = True
                    cols[j][od(board[i][j])] = True
                    recs[i//3*3+j//3][od(board[i][j])] = True
                    if dfs(idx+1):#一条路能走到底就不会把这条路中间的节点重置
                        return True
                    rows[i][od(board[i][j])] = False
                    cols[j][od(board[i][j])] = False
                    recs[i//3*3+j//3][od(board[i][j])] = False
                    board[i][j] = '.'
            return False
        dfs(0)
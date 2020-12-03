class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    if i==0 or j==0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = min(int(matrix[i-1][j]),int(matrix[i][j-1]),int(matrix[i-1][j-1]))+1
                else:
                    matrix[i][j]=0
                res = max(matrix[i][j]**2,res)
                    
        return res
s = Solution()
mat = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
s.maximalSquare(mat)
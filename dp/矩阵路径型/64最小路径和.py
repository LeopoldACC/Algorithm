class Solution:
    def minPathSum(self, grid) -> int:
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0:
                    grid[i][j] += grid[i][j-1] if j>0 else 0
                if j==0:
                    grid[i][j] +=grid[i-1][j] if i>0 else 0
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
s = Solution()
s.minPathSum(grid)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        f = [[0]*(n+1) for _ in range(n)]
        # f[i][j]表示从[i,j]赢得对手最多
        # 则对手赢我们最多为f[i+1][j] 或f[i][j-1]
        # 则f[i][j] = max(nums[i]-f[i+1][j],nums[j]-f[i][j-1])
        for i in range(n):
            f[i][i] = piles[i]
        
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                f[i][j] = max(piles[i]-f[i+1][j],piles[j]-f[i][j-1])
        return f[0][n-1]>=0
        
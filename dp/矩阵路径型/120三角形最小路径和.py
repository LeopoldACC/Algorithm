class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[-1][i] = triangle[-1][i]
        
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[i][j]=triangle[i][j] +max(dp[i+1][j],dp[i+1][j+1])
        
        return dp[0][0]
so =Solution()
arr = [[2],[3,4],[6,5,7],[4,1,8,3]]
so.minimumTotal(arr)
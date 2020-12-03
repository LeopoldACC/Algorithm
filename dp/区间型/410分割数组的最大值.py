class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        prefix = [0]+nums
        for i in range(1,n+1):
            prefix[i]+=prefix[i-1]
        dp = [[float('inf')]*(m+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1,n+1):
            for j in range(1,min(i,m)+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j],max(dp[k][j-1],prefix[i]-prefix[k]))#前i个划分为j个子数组和的最大值最小
        
        return dp[n][m]
        
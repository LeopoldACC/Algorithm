class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(1,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],j*(i-j),(i-j)*dp[j])
        return dp[n]
#漏了 j*(i-j) 没考虑不把j分开的情况  比如 3 = 1*2 =2 > 1* (1*1) = 1的
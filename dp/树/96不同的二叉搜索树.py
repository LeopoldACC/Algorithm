class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0]=1
        for i in range(1,n+1):#从1到n    由于
            for j in range(1,i+1):#对取根为0-i情况下的数量求和
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]
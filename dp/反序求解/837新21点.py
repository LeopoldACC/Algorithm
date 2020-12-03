class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K==0:
            return 1.0
        dp = [0.0]*(K+W+1)
        for i in range(K,min(K+W-1,N)+1):
            dp[i]=1.0
        dp[K-1] = min(N-K+1,W)/W
        for i in range(K-2,-1,-1):
            dp[i] = dp[i+1]+(dp[i+1]-dp[i+W+1])/W
        return dp[0]
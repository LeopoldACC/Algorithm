class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        dp = [[0]*3 for _ in range(n)]
        ## 0:第i天不持有股票，不买卖 1:第i天买入->第i-1天不能是2 2:第i天不持有股票，卖出 第i-1天只能是1
        dp[0][0]=0
        dp[0][1]=-prices[0]
        dp[0][2]=0
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][2])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2] = dp[i-1][1]+prices[i]
        return max(dp[:][-1])
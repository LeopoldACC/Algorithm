class Solution:
    def mincostTickets(self, days, costs):
        # dp[i] =min(dp[i-1]+cost[0],dp[i-7]+cost[1],dp[i-30]+cost[2])
        #
        def getdp(index,dp):
            if index<0:
                return 0
            else:
                return dp[index]
        #return 0 if index<0 else dp[index]
        dp = [0]*(days[-1]+1)
        travel = [False]*(days[-1]+1)
        for day in days:
            travel[day]=True
        #travel = [True if i in days else False for i in range(len(dp))]
        #[1,4,6,7,8,20]
        #第1天 2 第4天 2+2 第6天2+2+2 第7天7<2+2+2+2 第8天 2+7<2+2+2+2+2
        for i in range(len(dp)):
            if not travel[i]:
                dp[i]=dp[i-1]#没到需要经过的天就不花钱
            else:#getdp(起点,dp) 如果起点<0 那么就是从最开始，所以return 0 
                dp[i] = min(getdp(i-1,dp)+costs[0],getdp(i-7,dp)+costs[1],getdp(i-30,dp)+costs[2])
        #dp[i] = min(getdp(i-1,dp)+costs[0],getdp(i-7,dp)+costs[1],getdp(i-30,dp)+costs[2]) if travel[i] else dp[i-1]
        return dp[-1]
#https://leetcode-cn.com/problems/minimum-cost-for-tickets/solution/cdong-tai-gui-hua-by-d_dong/
s = Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(s.mincostTickets(days,costs))
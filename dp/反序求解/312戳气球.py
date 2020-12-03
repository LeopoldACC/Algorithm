class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0]*(n+2) for _ in range(n+2)]
        #从最后一步开始思考 k为i->j中最后戳破的气球，那么戳破k时它的左右就分别是nums[i]和nums[j] 那么dp[i][j] = dp[i][k]+nums[i]*nums[k]*nums[j] + dp[k][j]
        for i in range(n,-1,-1):#从下至上 确保dp[k][j]有值 从左至右确保dp[i][k]有值
            for j in range(i+1,n+2):
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j],dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])

        return dp[0][n+1]

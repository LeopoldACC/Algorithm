class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n < 3:
            return max(nums)
        dp = [0]*n
        dp[0],dp[1]=nums[0],max(nums[0],nums[1])###考虑[2,1,1,2]的情况 首先第3个不会因为我们初始化为[2,2,0,0]所影响,那第4个就会被影响了
        for i in range(2,n):#dp[3] = max(dp[2],dp[1]+nums[3]),这时dp[1]并不能代表前2个房子中偷盗完后最大收益 
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])#为什么第三个不受影响？ 第三天不偷 dp[1],dp[0]+nums[2] ,而dp[1]代表的是前两天中最大的收益，所以选取max(nums[0].nums[1])
        return dp[-1]


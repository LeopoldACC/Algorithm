class Solution0:
    def maxNonOverlapping(self, nums, target: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            cnt = 0
            l,r=i,i+1
            while r<=n:
                if sum(nums[l:r])==target: 
                    cnt+=1
                    l=r
                r+=1
            res = max(res,cnt)
        return res
class Solution:
    def maxNonOverlapping(self, nums, target: int) -> int:
        n = len(nums)
        prefix_sum = nums[:]
        res = 0
        for i in range(1,n):
            prefix_sum[i]+=prefix_sum[i-1]
        prefix_sum = [0]+prefix_sum
        dp = [[0]*(n+1) for _ in range(n+1)]
        #dp[i][j]表示 nums[i:j+1]最大有几个不重叠非空子数组 dp[0][n-1] 
        # dp[i][j] = dp[i][k]+dp[k+1][j]
        for i in range(1,n+1):
            dp[i][i] = 1 if nums[i-1]==target else 0
            print(prefix_sum[n]-prefix_sum[i-1],i)
            if prefix_sum[n]-prefix_sum[i-1]==target:
                dp[i][n]=1
        for i in range(n,0,-1):
            for j in range(i+1,n+1):
                for k in range(i,j):
                    if prefix_sum[k]-prefix_sum[i-1]==target and dp[i][k] == 0:
                        dp[i][k] = 1
                    if prefix_sum[j]-prefix_sum[k]==target and dp[k+1][j] == 0:
                        dp[k+1][j]=1
                    dp[i][j] = max(dp[i][j],dp[i][k]+dp[k+1][j])
        
        return dp[1][n]
s = Solution()
nums = [1,1,1,1,1]
target = 2
# nums = [-2,6,6,3,5,4,1,2,8]
# target = 10
nums = [-5,5,-4,5,4]
target = 5
s.maxNonOverlapping(nums,target)
class Solution:
    def maxSumAfterPartitioning(self, A, K: int) -> int:
        n = len(A)
        dp = [0]*(n+1)
        for i in range(1,n+1):
            mx = -float('inf')
            for j in range(i-1,max(i-K-1,-1),-1):
                mx = max(mx,A[j])
                dp[i] = max(dp[i],dp[j]+mx*(i-j))
        return dp[n]
# 状态转移
# 假设前面的区间都放好了 
# 所以我们只考虑最后一个区间从哪开始划分 
# 所以遍历[i-K,i-1] dp[i] = max(dp[j]+max(A[j:i])*(i-j)) 
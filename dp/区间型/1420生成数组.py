class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return 0
        dp = [[[0] * (m) for _ in range(k + 1)] for __ in range(n)]
        dp[0][1] = [1] * m
        
        for i in range(1, n):
            for j in range(1, k + 1):
                for p in range(m):
                    dp[i][j][p] = sum(dp[i - 1][j - 1][: p]) + dp[i - 1][j][p] * (p + 1)
                    dp[i][j][p] %= 1e9+7
                    
        return int(sum(dp[-1][-1])%(1e9+7))


# 链接：https://leetcode-cn.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/solution/jian-dan-san-wei-dong-tai-gui-hua-by-coldme-2/

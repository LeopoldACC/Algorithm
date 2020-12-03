class Solution:
    def f(self, n, i, k):
        if (self.tmp[n][i][k] != -1):
            return self.tmp[n][i][k]
        if n == 0 or k == 0 or i == 0:
            self.tmp[n][i][k] = 0
            return 0
        if n == 1 and k == 1:
            self.tmp[n][i][k] = 1
            return 1
        r=0
        for j in range(1, i):
            r += self.f(n-1, j, k-1)
            r %= 1000000007
        r += self.f(n-1, i, k)*i
        r %= 1000000007
        self.tmp[n][i][k] = r
        return r
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.tmp = [[[-1 for t in range(k+1)] for j in range(m+1)] for i in range(n+1)]
        r = 0
        for i in range(1, m+1):
            r += self.f(n, i, k)
            r %= 1000000007
        return r
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return 0
        dp = [[[0] * (m) for _ in range(k + 1)] for __ in range(n)]
        dp[0][1] = [1] * m
        
        for i in range(1, n):
            for j in range(1, k + 1):
                for p in range(m):
                    dp[i][j][p] = sum(dp[i - 1][j - 1][: p]) + dp[i - 1][j][p] * (p + 1)###乘p+1是因为p是从0到m-1 也就是比最大值p小1，但索引位置是第p+1个
                    dp[i][j][p] %= 1e9+7###最大值p在数组末尾（搜寻代价+1）
                                        ###+最大值p在前i-1个元素中，数组末尾可以从1到p选（搜寻代价不变，原来就是j，且最大值为p）
                    
        return int(sum(dp[-1][-1])%(1e9+7))

# 链接：https://leetcode-cn.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/solution/jian-dan-san-wei-dong-tai-gui-hua-by-coldme-2/
# 当最大值 i 恰好只出现在数组末尾时，前n-1个元素都小于i就可以满足，
# 构造的方法有 \sum_{j=1}^{i-1}dp[n-1][j][k-1]
# 而当最大值出现在前n−1个元素之中时，数组末尾的元素可以从1到i中任意选取，即有 i×dp[n-1][i][k] 种构造方法。

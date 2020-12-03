class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0]=1
        for i in range(1,n+1):#对于1->i构成的所有树的集合种数
            for j in range(1,i+1):#遍历1->i中的所有j为根节点 ->左子树数量dp[j-1]*右子树数量dp[i-1]
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]
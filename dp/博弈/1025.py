class Solution:
    def divisorGame(self, N: int) -> bool:
        if N<2: return False

        dp = [False] * (N+1)
        dp[0] = False
        dp[1] = False

        for i in range(2,N+1):
            for j in range(1,i//2+1):##范围要多开一个1确保能到i//2
                if i%j==0:
                    dp[i] = dp[i] or not dp[i-j]## i-j代表甲方拿完j后乙方在i-j的条件下必输->甲方在这种情况下必赢
                    if dp[i]:#从该路径下 在i能获胜
                        break
        return dp[N]


s = Solution()
s.divisorGame(2)
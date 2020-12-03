class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == p[j-1] or p[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        # dp[i-1][j],表示*代表非空任何字符,例如abcd,ab* 总会在一个c 和*的地方先通过dp[1][2] = dp[1][2-1]变True  然后后面dp[i-1][j]一直是true的
        # ​dp[i][j-1],表示*代表是空字符,例如ab,ab*  
        return dp[-1][-1]
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True
        for i in range(1,n):
            print(dp[0][i-1] and p[i]=="*")
            dp[0][i+1] = dp[0][i-1] and p[i]=="*"##第一个=号写成了==

        print(dp)
        for i in range(m):
            for j in range(n):
                if s[i]==p[j] or p[j]==".":
                    dp[i+1][j+1] = dp[i][j]
                elif p[j]=="*":
                #第一种情况 i=1 c j=3 ..*  dp[i][j] = dp[i][j-2]   p[j-1]* = 空      ..* = .
                #第二种情况 p[j-1] == s[i] or p[j-1] == "." 即 *的前一位p[j-1]可以与s[i]匹配时,只要s[:i]与p[:j+1]匹配的了,*再把p[j-1]复制后也就把s[i]与p[j]匹配了
                # dp[i][j] = dp[i-1][j]    p[j-1]* = p[j-1]  ..* = .. 所以此时能匹配的条件就是 p[j-1]==s[i] or '.'
                # or dp[i][j] = dp[i][j-1]   p[j-1]* = p[j-1]
                # or dp[i][j] = dp[i][j-1]   p[j-1]* = 空
                    if p[j-1]!=s[i]:
                        dp[i+1][j+1] = dp[i+1][j-1]
                    if p[j-1] == s[i] or p[j-1] == ".":##不能el 为什么 因为p[j-1]!=s[i]但p[j-1]=='.'的时候是满足的
                        dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j] or dp[i+1][j-1]
                        
        return dp[-1][-1]
so = Solution()
s = "aab"
p = "c*a*b"
so.isMatch(s,p)
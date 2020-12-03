class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=True
            if i+1<n and s[i]==s[i+1]:
                dp[i][i+1]=True
        res = s[0]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n): 
                if j-i<3:
                    if s[i]==s[j]:
                        dp[i][j]=True
                else:
                    dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
                if j-i+1>len(res) and dp[i][j]:
                    res = s[i:j+1]
        return res
    
s =Solution()
s.longestPalindrome("abcba")
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not s:
            return ""
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
        l,r=0,0
        res = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i]==s[j]:
                    if j-i<=2:
                        dp[i][j] = j-i+1
                    else:
                        if dp[i+1][j-1]+2 == j-i+1:#判断i~j是不是回文串 不仅靠s[i]==s[j] 中间s[i+1:j-1]也得是 所以加起来的长度要==j-i+1
                            dp[i][j] = dp[i+1][j-1]+2
                if dp[i][j] > res:
                    res = dp[i][j]
                    l,r = i,j
        return s[l:r+1]
so = Solution()
st = "abcda"
so.longestPalindrome(st)
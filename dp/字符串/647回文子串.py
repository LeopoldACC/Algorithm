class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        f = [[False]*n for _ in range(n)]

        for i in range(n):
            f[i][i] = True
        res = n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    f[i][j] = f[i+1][j-1] or j-i==1
                if f[i][j]:
                    res+=1
        return res
s = Solution()
string = "abc"

s.countSubstrings(string)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]
        
        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1
        
        return True
#dp[i][j] 表示字符串 t 中从位置 i 开始往后字符 j 第一次出现的位置。
# t[i] == j -> dp[i][j] = i 当前位置是j,dp[i][j] = i
# 否则 dp[i][j] = dp[i+1][j] 否则第一次出现的位置在后面 ，所以要从后往前dp
#所以对t建状态转移 
#对s逐一遍历 start = 0 dp[start][s[i]]为s[i]在t中start及start之后第一次出现的位置 
# 如果dp[start][s[i]]=m，则说明t中start及start之后没有出现s[i]
# 每一次弄完之后start要更新为dp[start][s[i]]+1 ,dp[start][s[i]]已经匹配上了s[i],所以要+1才能用于匹配下一次的s[i+1]
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m,n = len(s),len(t)
        dp = [[0] * 26 for _ in range(n+1)]
        dp[n] = [m]*26
        for i in range(n-1,-1,-1):
            for j in range(26):
                if j==ord(t[i])-ord('a'):
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i+1][j]
        add = 0
        for i in range(m):
            if dp[add][ord(s[i])-ord('a')] == m:
                return False
            add = dp[add][ord(s[i])-ord('a')]+1#思考为什么要+1 因为这一次已经把s[i]匹配完了,所以下一次add不能再从dp[add][ord(s[i])-ord('a')]开始

        return True

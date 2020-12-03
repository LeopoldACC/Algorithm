class Solution1:#超时
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        st = [False]*m
        self.res = 0
        def dfs(path,start,idx):
            if m-start<n-idx:
                return
            if idx==n:
                if path == t:
                    self.res+=1
                return
            for i in range(start,m):
                if not st[i] and s[i]==t[idx]:
                    path+=s[i]
                    st[i] = True
                    dfs(path,i+1,idx+1)
                    path=path[:-1]
                    st[i] = False
                    
        dfs('',0,0)
        return self.res

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        # f[i][j] s[:i]中 包含t[:j]的子序列个数
        # 闫式dp分析
        # 子集划分 -- s[i]用/不用
        # 1 if s[i]!=t[j]:如果s[i]!=t[j] 则s[:i]中匹配t[:j]子序列个数==s[:i-1]中匹配t[:j]子序列个数
        #       f[i][j] = f[i-1][j]
        # 2 if s[i]==t[j]:
        #       f[i][j] = f[i-1][j-1] + f[i-1][j]
        # 2.1用s[i]     f[i-1][j-1] 则s[:i]中匹配t[:j]子序列个数==s[:i-1]中匹配t[:j-1]子序列个数
        # 2.2不用s[i]   f[i-1][j]   则s[:i]中匹配t[:j]子序列个数==s[:i-1]中匹配t[:j]子序列个数
        # 初始化
        # f[0][j] s[:0]=='' 中匹配 t[:j]子序列个数=0
        # f[i][0] s[:i] 中匹配t[:0]=='' 子序列个数=1(空串==s的一个子串)
        f = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            f[i][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    f[i][j] = f[i-1][j-1]+f[i-1][j]
                else:
                    f[i][j] = f[i-1][j]
        return f[m][n]
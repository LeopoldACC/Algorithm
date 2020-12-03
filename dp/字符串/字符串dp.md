# Leetcode 115不同的子序列  
```
f[i][j] s[:i]中 包含t[:j]的子序列个数
闫式dp分析
子集划分 -- s[i]用/不用
1 if s[i]!=t[j]:如果s[i]!=t[j] 则s[:i]中匹配t[:j]子序列个数==s[:i-1]中匹配t[:j]子序列个数
        f[i][j] = f[i-1][j]
2 if s[i]==t[j]:
        f[i][j] = f[i-1][j-1] + f[i-1][j]
2.1用s[i]     f[i-1][j-1] 则s[:i]中匹配t[:j]子序列个数==s[:i-1]中匹配t[:j-1]子序列个数
2.2不用s[i]   f[i-1][j]   则s[:i]中匹配t[:j]子序列个数==s[:i-1]中匹配t[:j]子序列个数
初始化
f[0][j] s[:0]=='' 中匹配 t[:j]子序列个数=0
f[i][0] s[:i] 中匹配t[:0]=='' 子序列个数=1(空串==s的一个子串)
```
```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
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
```

# dfs回溯/剪枝
## 131分割回文串
对于当前s 

1. 将其分为s[:i]和s[i:]
2. 如果s[:i]是回文串,则path+s[:i]
3. s = s[i:] 继续往下搜
4. 直到s==''时 res.append(path)


```python 
class Solution:
    def partition(self, s: str):
        res = []
        
        def dfs(s, path):
            if not s:
                res.append(path)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], path + [s[:i]])
        dfs(s, [])
        return res
```
##132分割回文串2
```python
dfs超时
class Solution:
    def minCut(self, s: str) -> int:
        self.res = len(s)
        def dfs(s,path):
            if s=='':
                self.res = min(self.res,len(path)-1)
            for i in range(1,len(s)+1):
                if s[:i]==s[:i][::-1]:
                    dfs(s[i:],path+[s[:i]])
        dfs(s,[])
        return self.res
dp
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        f = [[False]*n for _ in range(n)]
        cnt = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[i]==s[j] and (i-j<=2 or f[j+1][i-1]):
                    f[j][i] = True
                    # 说明s[j:i]不用分割 s[:i]分割数=s[:j]分割数+1
                    if j==0:
                        cnt[i] = 0
                    else:
                        cnt[i] = min(cnt[i],cnt[j-1]+1)
        return cnt[n-1]
```

class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        next = [-1] * n
        for i in range(1,n):
            j=next[i-1]###j的初始化不记得---> 首先j是s[:i-1]部分最长前后缀 所以j初始化为next[i-1]
            while j>-1 and s[j+1]!=s[i]:###为什么 j = next[j] aaaab [-1, 0, 1, 2, -1]  aaaab 前后缀j=2 ，所以j=next[2]=1再去判断s[1+1]
                j = next[j]### 前缀新添加s[j+1] 后缀新添加s[i] 两者不等时 j 要回到上一个位置 j的上一个位置next[j]
                            ### j就一直减到j=-1或者s[j+1]=s[i] 
            if s[j+1] == s[i]: ### s[j+1]与s[i]匹配失败next[j]存的是
                next[i] = j+1###next[i]而不是next[j]
            print('i:',i,'j:',j,'s[j+1]:',s[j+1],'s[i]:',s[i],'next:',next)
        return s[:next[-1]+1] 
s = Solution()
sr = "ababcababak"
s.longestPrefix(sr)

class Solution:二刷
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        next = [-1] * n 
        for i in range(1,n):
            j = next[i-1]
            while j>-1 and s[j+1]!=s[i]:
                j=next[j]
            #else:###不是else,如果是else的话就是满足两个条件 j<=-1 or s[j+1] ==s[i]了
            if s[j+1]==s[i]:
                ###j = j+1###j这里不用更新，循环的下一次会j=next[i-1]更新
                next[i] = j+1

        return s[:next[-1]+1]
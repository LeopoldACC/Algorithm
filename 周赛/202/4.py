class Solution0:#O(n)
    def minDays(self, n: int) -> int:
        f = [float('inf')]*(n+1)
        f[0] = 0
        for i in range(n+1):
            f[i] = min(f[i-1]+1,f[i])
            if i%2==0:
                f[i] = min(f[i//2]+1,f[i])
            if i%3==0:
                f[i] = min(f[i//3]+1,f[i])
        return f[n]
# class Solution1:
#     def minDays(self, n: int) -> int:
#         res = 0
#         maxi = 3**100
#         while n:
#             if maxi%n==0:
#                 while n:
#                     n//=3
#                     res+=1
#                 return res
#             if n &(n-1)==0:
#                 while n:
#                     n//=2
#                     res+=1
#                 return res
#             if n%3==0:
#                 n=n//3
#                 res+=1
#                 continue
#             if (n-1)%3==0 and (n-1)%2==0:
#                 n-=1
#                 n//=3
#                 res+=2
#                 continue
#             if n%2==0:
#                 n=n//2
#                 res+=1
#                 continue
#             n-=1
#             res+=1
#         return res
# 673
# 672 
# 336 224 事实是不知道什么应该优先
# 168 112 111
# 84  56  37
# 42  28
# 21  27
# 7   9
# 6   3
# 2   1
# 1
f = {}
class Solution:#right ans 
    def minDays(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n in f:
            return f[n]
        res = min(self.minDays(n//2)+n%2+1,self.minDays(n//3)+n%3+1)
        f[n] = res
        return self.minDays(n)
#很自然的想到 树的结构->dfs 每个结点三种选法 实际上就是两种选法->2个分支 
# //3 + 为了//3-n%3 +1
# //2 + 为了//2+n%2 +1
# 用f[i]记忆化剪枝->已经搜到过的值不再重复搜
s = Solution()
res = s.minDays(673)
print(res)
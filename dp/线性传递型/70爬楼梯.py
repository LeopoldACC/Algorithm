class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0]*(n+1)
        f[0]=1
        f[1]=1
        for j in range(2,n+1):
            f[j] += f[j-1]+f[j-2]        
        return f[n]
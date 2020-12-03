class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        a = b = 6
        
        while n > 1:
            n -= 1
            a,b = 2*a+2*b,2*a+3*b
        return (a+b)%MOD

class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        
        import sys   
        sys.setrecursionlimit(1000000)
        import functools
        @functools.lru_cache(None)
        def dp(i, pre):
            if i == n:
                return 1
            res = 0
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        if a != b and b != c and a != pre[0] and b != pre[1] and c != pre[2]:
                            res += dp(i + 1, (a, b, c))
                            res %= mod
            return res
        
        return dp(0, (-1, -1, -1)) % mod
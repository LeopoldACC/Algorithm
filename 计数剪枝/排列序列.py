class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # C = [[0]*(n+1) for _ in range(n+1)]
        # for i in range(n+1):
        #     C[i][0] = 1
        # for i in range(n+1):
        #     for j in range(i+1):
        #         C[i][j] = C[i-1][j] + C[i-1][j-1]
        if n == 0:
            return ""
        fac = [1 for i in range(n+1)]
        for i in range(2,n+1):
            fac[i]=fac[i-1]*i
        print(fac)          
        vis = set()
        self.res = None
        self.k = k
        def dfs(path):
            if len(path) == n:
                self.res = path 
                return 
            for i in range(1,n+1):
                if i not in vis:
                    if fac[n-len(path)-1]>=self.k:
                        path+=str(i)
                        vis.add(i)
                        dfs(path)
                        return 
                        # 已经缩小到第len(path)位要用i了 所以就不存在说这一位再换其他数了
                        # path = path[:-1]
                        # vis.remove(i)
                    else:
                        self.k-=fac[n-len(path)-1]
                        continue
        dfs("")
        return self.res

so = Solution()
so.getPermutation(3,3)
class Solution:
    def findLength(self, A, B) -> int:
        m = len(A)
        n = len(B)
        res = 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if A[i] == B[0]:
                dp[i][0] = 1
        for j in range(n):
            if B[j] == A[0]:
                dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                if A[i] == B[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                res = max(res,dp[i][j])

        return res

so = Solution()
A = [0,0,0,0,1]
B = [1,0,0,0,0]
so.findLength(A,B)
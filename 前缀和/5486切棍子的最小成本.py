class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        #dp[i][j] 为切第i根棍子到第j根棍子的最小成本
        #dp[i][j] = min(dp[i][k]+dp[k][j]) for k in range(i,j)
        #[0,1,3,4,5,7] 
        #dp[4][5] = min(dp[4][5]+dp[5][5]+cuts[5]-cuts[4],0) = 0
        #dp[3][4] = min(dp[3][4]+dp[4][4]+cuts[4]-cuts[3],0) = 0
        #dp[3][5] = min(dp[3][4]+dp[4][5]+cuts[5]-cuts[3],inf) = 3
        #dp[2][3] = min(dp[2][3]+dp[3][3]+cuts[3]-cuts[2],0) = 0
        #dp[2][4] = min(dp[2][3]+dp[3][4]+cuts[4]-cuts[2],inf) = 2
        #dp[2][5] = min(dp[2][3]+dp[3][5]+cuts[5]-cuts[2],dp[2][4]+dp[4][5]+cuts[5]-cuts[2],inf) = dp[2][4]+7-3 = 6
        #dp[1][2] = 0
        #dp[1][3] = min(dp[1][2]+dp[2][3]+cuts[3]-cuts[1],inf) = 3
        #dp[1][4] = min(dp[1][2]+dp[2][4]+cuts[4]-cuts[1],dp[1][3]+dp[3][4]+cuts[4]-cuts[1],inf) = 2+5-1=6
        #dp[1][5] = min(dp[1][2]+dp[2][5]+cuts[5]-cuts[1],dp[1][3]+dp[3][5]+cuts[5]-cuts[1],dp[1][4]+dp[4][5]+cuts[5]-cuts[1],inf) = 6+6=12
        #dp[0][1] = 0
        #dp[0][2] = min(dp[0][1]+dp[1][2]+cuts[2]-cuts[0],inf) = 3
        #dp[0][3] = min(dp[0][1]+dp[1][3]+cuts[3]-cuts[0],dp[0][2]+dp[2][3]+cuts[3]-cuts[0],inf) = 3+4 = 7
        #dp[0][4] = min(dp[0][1]+dp[1][4]+cuts[3]-cuts[0],dp[0][2]+dp[2][4]+cuts[4]-cuts[0],dp[0][3]+dp[3][4]+cuts[4]-cuts[0],0) = min(6,5,7)+5 = 10
        #dp[0][5] = min(dp[0][1]+dp[1][5]+cuts[3]-cuts[0],dp[0][2]+dp[2][5]+cuts[5]-cuts[0],dp[0][3]+dp[3][5]+cuts[5]-cuts[0],dp[0][4]+dp[4][5]+cuts[5]-cuts[0],inf) = min(12,9,10,10)+7 = 16
        #dp[0][2] + dp[2][5] -> 0->3 + 3->7 -> 3+dp[2][4]+dp[4][5]+7-3 = 3+0+0+4-2+7-3=9 
        cuts = [0]+cuts+[n]
        m = len(cuts)
        dp = [[float('inf')] * m for _ in range(m)]
        cuts.sort()
        for i in range(m-1):
            dp[i][i+1] =0  
        for i in range(m,-1,-1):
            for j in range(i+1,m):
                for k in range(i+1,j):
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j]+cuts[j]-cuts[i])
        print(cuts)
        print(dp)
        return dp[0][m-1]
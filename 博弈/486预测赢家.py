class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        #f[i][j] 代表从i->j这个数组从两端选 赢得最多->我-对手
        #则对手赢我的 == 从f[i+1][j] 或f[i][j-1]中选的
        # 我赢对手的 = 当前选的nums[i] - 对手赢我的f[i+1][j]
        #           or当前选的nums[j] - 对手赢我的f[i][j-1]
        #f[i][j] = max(nums[i] - f[i+1][j],nums[j]-f[i][j-1])
        for i in range(n):
            f[i][i] = nums[i]
        for i in range(n-2,-1,-1):
            for j in range(i,n):
                f[i][j] = max(nums[i]-f[i+1][j],nums[j]-f[i][j-1])
        return f[0][n-1]>=0
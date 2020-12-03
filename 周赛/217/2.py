class Solution:
    def mostCompetitive(self, nums, k: int):
        res = []
        def dfs(nums,t):
            if not nums:
                return
            n = len(nums)
            idx = nums[:n-(t-1)].index(min(nums[:n-(t-1)]))
            res.append(nums[idx])
            dfs(nums[idx+1:],t-1)
        dfs(nums,k)
        return res
so = Solution()
nums = [3,5,2,6]
k = 2
so.mostCompetitive(nums,k)
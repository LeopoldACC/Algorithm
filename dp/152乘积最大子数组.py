class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp_max = [-float('inf')]*len(nums)
        dp_min = [float('inf')]*len(nums)
        dp_max[0],dp_min[0]= nums[0],nums[0]
        for i in range(1,len(nums)):
            dp_max[i] = max(dp_min[i-1]*nums[i],dp_max[i-1]*nums[i],nums[i])##是跟nums[i]比而不是dp[i]
            dp_min[i] = min(dp_min[i-1]*nums[i],dp_max[i-1]*nums[i],nums[i])##写了两个dp_max
        return max(dp_max)##dp_max[-1]
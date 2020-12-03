class Solution:
    def canPartition(self, nums) -> bool:
        sums = 0
        for num in nums:
            sums+=num
        if sums%2!=0:return False
    
        half = sums//2
        f = [False] * (half+1)
        f[0] = True
        for i in range(len(nums)):
            for j in range(half,nums[i]-1,-1):
                f[j] |= f[j-nums[i]]
        return f[half]
s = Solution()
nums = [1, 5, 11, 5]
res =s.canPartition(nums)
print(res)
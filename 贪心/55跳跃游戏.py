class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rmax = nums[0]
        n = len(nums)
        for i in range(n):
            if i <=rmax:
                rmax = max(i+nums[i],rmax)
                if rmax>=n-1:
                    return True
        return False
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        for i in range(1,n):
            res ^= nums[i]
        return res
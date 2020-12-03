class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i]>0 and nums[i]-1<n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        for i in range(n):
            if i+1!=nums[i]:
                return i+1
        return n+1
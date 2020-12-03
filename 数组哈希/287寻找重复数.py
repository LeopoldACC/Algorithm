class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i]-1 != i:
                if nums[nums[i]-1] == nums[i]:
                    return nums[i]
                nums[nums[i]-1] , nums[i] = nums[i] , nums[nums[i]-1]
        
        return None
# [2, 3, 1, 0, 2, 5, 3]为例
# 第一轮就排好序 [0, 1, 2, 3, 2, 5, 3]
# 之后等i到第5个2的时候才返回nums[4]=2
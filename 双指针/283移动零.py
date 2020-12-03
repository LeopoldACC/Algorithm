class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        n = len(nums)
        
        for r in range(n):
            if nums[r]!=0:
                nums[l]=nums[r]
                if l!=r:
                    nums[r]=0
                l+=1#只有在出现一段0的时候才会有r>l
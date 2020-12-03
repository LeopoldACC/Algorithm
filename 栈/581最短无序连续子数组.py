class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack,l,r = [],len(nums),0
        for i in range(len(nums)):
            while stack and nums[i]<nums[stack[-1]]:
                l=min(l,stack.pop())
            stack.append(i)
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i]>nums[stack[-1]]:
                r = max(r,stack.pop())
            stack.append(i)
        return r-l+1 if r-l>0 else 0   
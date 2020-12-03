class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,0
        n = len(nums)

        p = 0
        lens = 0
        while r<n:
            while l<n and r<n and nums[l]==nums[r]:
                r+=1
            
            lens+=2 if r-l>2 else r-l
            cur = 2 if r-l>2 else r-l
            while cur:
                nums[p] = nums[l]
                p+=1
                cur-=1
            l = r
        return lens
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        n = len(nums)
        l,r = 0,n
        while l<r:
            mid = (l+r)//2
            if nums[mid]>=target:
                r=mid
            else:
                l=mid+1
        if l<n and nums[l] == target:
            p = l
            while p<n and nums[p]==target:
                p+=1
            return [l,p-1]
        return [-1,-1]
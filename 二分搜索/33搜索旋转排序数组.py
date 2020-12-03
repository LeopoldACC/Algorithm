class Solution:
    def search(self, nums, target) -> int:
        if not nums:
            return -1
        l,r = 0,len(nums)-1
        while l+1<r:
            mid = (l+r)//2
            if nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid]<target<=nums[r]:
                    l = mid
                else:
                    r = mid
        
        if nums[l]==target:
            return l 
        if nums[r]==target:
            return r
        return -1
# 20201109二刷
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if nums[0]>nums[-1]:
            for i in range(1,n):
                if nums[i]<nums[i-1]:
                    p = i-1
                    break
            if target<nums[p+1] or target>nums[p]:
                return -1
            if target<=nums[-1]:
                l,r = p+1,n 
            else:
                l,r = 0,p
            while l<r:
                mid = (l+r)//2
                if nums[mid]<target:
                    l = mid+1
                else:
                    r = mid
            return l if nums[l]==target else -1
        else:
            l,r = 0,n-1
            while l<r:
                mid = (l+r)//2
                if nums[mid]<target:
                    l = mid+1
                else:
                    r = mid
            return l if nums[l]==target else -1

s = Solution()
nums = [4,5,6,7,0,1,2]
t = 0
s.search(nums,t)
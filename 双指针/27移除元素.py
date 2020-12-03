class Solution:
    def removeElement(self, nums, val: int) -> int:
        l,r,n = 0,0,len(nums)
        p = 0
        while r<n:
            # 找第一个等于val的位置
            while l<n and nums[l]!=val:
                l+=1
            r=l
            while r<n and nums[r]==val:
                r+=1
            cur = r
            p += r-l
            while cur<n and nums[cur]!=val:
                nums[cur-p] = nums[cur]
                cur+=1
            l=cur
        return p
s = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
s.removeElement(nums,val)
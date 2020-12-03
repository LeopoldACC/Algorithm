class Solution:###最终版
    def minSubsequence(self, nums):
        nums = sorted(nums)
        prefix_sum = nums[:]
        for i in range(len(nums)-2,-1,-1):
            prefix_sum[i]+=prefix_sum[i+1]
        index = -1
        for i in range(len(nums)-1,-1,-1):
            if prefix_sum[i]>prefix_sum[0]//2:
                index = i
                break
        return nums[index:][::-1]
class Solution0:
    def minSubsequence(self, nums):
        nums = sorted(nums)
        prefix_sum =nums[:]
        for i in range(len(nums)):
            prefix_sum[i]+=nums[i]
        target = prefix_sum[-1]//2
        index = self.bisec(prefix_sum,target)
        return nums[index:][::-1]
        
    def bisec(self,prefix,target):
        start,end = 0,len(prefix)-1
        while start+1<end:
            mid = (start+end)//2
            if prefix[mid]<=target:
                start = mid
            else:
                end = mid
        return end if prefix[end]>target else start
    
s = Solution()
s.minSubsequence([4,4,7,6,7])
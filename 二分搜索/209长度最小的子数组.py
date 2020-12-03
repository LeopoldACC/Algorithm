class Solution:
    def minSubArrayLen(self, s: int, nums):
        res = float('inf')
        prefix_sum = [0]+nums[:]
        n = len(nums)
        for i in range(1,n+1):
            if nums[i-1]>=s:
                return 1
            prefix_sum[i]+=prefix_sum[i-1]
        for i in range(n+1):
            for j in range(i+1,n+1):
                if prefix_sum[j]-prefix_sum[i]>=s:
                    res=min(res,j-i)
        
        return res if res!=float('inf') else 0
##超出时间限制
class Solution1:##要求nlogn 然后发现前缀和数组是个单调的，所以可以想到二分
    def minSubArrayLen(self, s: int, nums):
        res = float('inf')
        prefix_sum = [0]+nums[:]
        n = len(nums)
        for i in range(1,n+1):
            if nums[i-1]>=s:
                return 1
            prefix_sum[i]+=prefix_sum[i-1]
        for i in range(n+1):
            l,r = i,n
            while l<r:
                mid = (l+r)//2
                if prefix_sum[mid]-prefix_sum[i]<s:
                    l = mid+1
                else:
                    r = mid
            if prefix_sum[l]-prefix_sum[i]>=s:
                res = min(res,l-i)
        print(res)
        return res if res!=float('inf') else 0
so = Solution1()
s = 15##11
nums = [1,2,3,4,5]
so.minSubArrayLen(s,nums)
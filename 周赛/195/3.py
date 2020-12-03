class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9+7
        n = len(nums)
        l,r = 0,n-1
        res = 0
        while l<=r:
            while l<=r and nums[l]+nums[r]>target:
                r-=1
            if r<l:
                break
            res+=(2**(r-l)) % mod
            res = res%mod
            l+=1
        return res
        
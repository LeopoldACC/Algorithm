class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not nums: return []
        nums.sort()
        if nums[0]>0: return []
        res = []
        for i in range(n-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                return res
            l,r = i+1,n-1
            while l<r:
                tmp = nums[i]+nums[l]+nums[r]
                if(tmp==0):
                    res.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[l]==nums[l+1]):
                        l=l+1
                    while(l<r and nums[r]==nums[r-1]):
                        r=r-1
                    l=l+1
                    r=r-1
                elif(tmp>0):
                    r=r-1
                else:
                    l=l+1
        return res
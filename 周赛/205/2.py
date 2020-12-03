class Solution:
    def numTriplets(self, nums1, nums2) -> int:
        return self.count(nums1,nums2)+self.count(nums2,nums1)
    def count(self, nums1, nums2):
        cnt1 = {}
        cnt2 = {}
        muti = {}
        k = 100007
        for num in nums1:
            cnt1[num] = cnt1.get(num,0)+1
        for num in nums2:
            cnt2[num] = cnt2.get(num,0)+1
        visit = set()
        for i in cnt2:
            for j in cnt2:
                if (i,j) in visit or (j,i) in visit:
                    continue
                visit.add((i,j))
                if i==j:
                    muti[i*j] = muti.get(i*j,0)+cnt2[i]*(cnt2[i]-1)//2
                    #WA  muti[i*j] = cnt2[i]*(cnt2[i]-1)//2
                    ##没考虑1*4 = 4 和 2*2重叠的情况,导致直接赋值覆盖原值而不是加上去
                else:
                    muti[i*j] = muti.get(i*j,0)+cnt2[i]*cnt2[j]
        res = 0
        for num in cnt1:
            num2 = num**2
            if num2 in muti:
                res+=cnt1[num]*muti[num2]
        return res
so = Solution()
a1 = [4,5,1,5,2]
a2 = [2,1,2,1]
so.numTriplets(a1,a2)
class Solution:
    def reversePairs(self, nums) -> int:
        tmp = list(set([2*x for x in nums]))
        tmp.sort()
        tot = len(tmp)
        tr = [0]*(tot+1)
        def get(x):
            i=x
            res = 0
            while i>0:
                res+=tr[i]
                i-=x&-x
            return res
        def add(x,c):
            i=x
            while i<=tot:
                tr[i]+=c
                i+=x&-x
        def bisect(x):
            l,r = 0,tot-1
            while l<r:
                mid = (l+r+1)//2
                if tmp[mid]<x:
                    l = mid
                else:
                    r = mid-1
            return l
        N = len(nums)
        res = 0
        for j in range(N-1,-1,-1):
            idx_cur,idx_cur2= bisect(nums[j]),bisect(nums[j]*2)
            res += get(idx_cur)
            add(idx_cur2+1,1)
        return res
so = Solution()
nums =[1,3,2,3,1]
so.reversePairs(nums)
class Solution:
    def reversePairs(self, nums) -> int:
        tmp = list(set(nums+[2*x for x in nums]))
        tmp.sort()
        tot = len(tmp)
        v = {tmp[i]:i+1 for i in range(len(tmp))}#离散化的时候要+1
        tr = [0]*(tot+1)
        def get(x):
            i=x
            res = 0
            while i>0:
                res+=tr[i]
                i-=i&-i
            return res
        def add(x,c):
            i=x
            while i<=tot:
                tr[i]+=c
                i+=i&-i
        N = len(nums)
        res = 0
        for j in range(N-1,-1,-1):
            res += get(v[nums[j]]-1)
            add(v[nums[j]*2],1)
        return res
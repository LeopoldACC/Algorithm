class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l,r = 0,len(A)
        while l<r:
            mid = (l+r)//2
            if A[mid]>=0:
                r = mid
            else:
                l = mid+1
        # print(l)
        if l==0:
            return [x**2 for x in A]
        p,q = l-1,l
        res = []
        while p>=0 and q<len(A):
            if -A[p]>=A[q]:
                res.append(A[q]**2)
                q+=1
            else:
                res.append(A[p]**2)
                p-=1
        while p>=0:
            res.append(A[p]**2)
            p-=1
        while q<len(A):
            res.append(A[q]**2)
            q+=1
        return res
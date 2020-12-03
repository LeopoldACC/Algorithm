class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        pre_sum = [0]+arr##不加零的话 [4,9,3] 10 为例 x=1,2的时候 pre_sum = 3而不是0
        n=len(arr)
        def bisect_l(x):
            l,r = 0,n-1
            while l<r:
                mid = (l+r)//2
                if arr[mid]>=x: r=mid
                else:l=mid+1
            return l
        def bisect_r(x):
            l,r = 0,n-1
            while l<r:
                mid = (l+r+1)//2
                if arr[mid]<=x: l=mid
                else:r=mid-1
            return l
        for i in range(1,n):
            pre_sum[i]+=pre_sum[i-1]

        r,res,diff = max(arr),0,target
        for x in range(1,r+1):
            i = bisect_r(x)
            cur = pre_sum[i]+(n-i)*x
            if abs(cur-target)<diff:
                res,diff = x,abs(cur-target)
        return res

class Solution:
    def findLengthOfShortestSubarray(self, arr) -> int:
        def bisect_l(t,l,r):
            while l<r:
                mid = (l+r)//2
                if arr[mid]<t:
                    l = mid+1
                else:
                    r = mid
            return l
        def bisect_r(t,l,r):
            while l<r:
                mid = (l+r)//2+1
                if arr[mid]>t:
                    r = mid-1
                else:
                    l = mid
            return l
        n = len(arr)
        if n<=1:return 0
        end = -1
        start = -1
        for i in range(n-1,0,-1):
            if(arr[i]<arr[i-1]):
                end = i
                break
        if -1==end:return 0
        for i in range(n-1):
            if(arr[i]>arr[i+1]):
                start = i
                break
        ns = start
        ne = end
        print(start,end,ns,ne)
        # [1,2,3,10,4,2,3,5]
        #去左右两边二分找arr[start] arr[end]
        #找第一个小于等于2的
        #找第一个大于等于3的
        res = float('inf')
        for i in range(start,-1,-1):
            r = bisect_l(arr[i],end,n-1)
            length = r-i if r==n-1 else r-i-1
            # print(length
            res = min(res,length)
        for i in range(end,n):
            l = bisect_r(arr[i],0,start)
            length = i-l if l==0 else i-l-1
            # print(length)
            res = min(res,length)
        return res
s = Solution()
arr =[6,3,10,11,15,20,13,3,18,12]
s.findLengthOfShortestSubarray(arr)
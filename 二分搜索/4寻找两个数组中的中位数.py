class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def findKth(k):
            i,j=0,0

            while True:
                if i==m:return nums2[j+k-1]###i==m而不是m-1
                if j==n:return nums1[i+k-1]
                if k==1:return min(nums1[i],nums2[j])###i，j是排完k//2一系列到只剩下一个的情况 15- >8 -> 4 ->2 ->1
                nexi,nexj = min(m-1,i+k//2-1),min(n-1,j+k//2-1)##防止一边过长一边过短
                p1,p2 = nums1[nexi],nums2[nexj]
                if p1<=p2:#比大小保证 只更新更小的index，更大的index就不会删除
                    k-=nexi-i+1
                    i = nexi+1
                else:
                    k-=nexj-j+1
                    j = nexj+1
        m,n=len(nums1),len(nums2)
        kt = m+n
        if (m+n)%2==0:
            return (findKth(kt//2)+findKth(kt//2+1))/2
        else:
            return findKth(kt//2+1)
n1 = [5,9]###可以发现，这种情况下，因为
n2 = [0,1,2,3,4,6,8,10,11]
s =Solution()
s.findMedianSortedArrays(n1,n2)
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i,j = 0,0
        m,n = len(nums1),len(nums2)
        s1,s2=0,0
        while i<m and j<n:
            if nums1[i]<nums2[j]:#直到nums[i]==nums[j]
                s1+=nums1[i]
                i+=1
            elif nums1[i]>nums2[j]:
                s2+=nums2[j]
                j+=1
            else:
                s1 = max(s1,s2)+nums1[i]
                s2 = s1
                i+=1
                j+=1
        while i<m:
            s1+=nums1[i]
            i+=1
        while j<n:
            s2+=nums2[j]
            j+=1
        return int(max(s1,s2)%(1e9+7))
class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        n = len(arr)
        l,r = 0,0
        while l<n:
            while l<n and arr[l]%2==0:
                l+=1
            r = l
            cnt = 0
            while r<n and arr[r]%2!=0:
                r+=1
                cnt+=1
            if cnt>=3:
                return True
            l = r
        return False
                
s = Solution()
arr = [2,6,4,1]
s.threeConsecutiveOdds(arr)
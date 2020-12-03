class Solution0:
    def getMaxLen(self, nums) -> int:
        n,l,r = len(nums),0,0
        res = 0
        while r<n:
            tmp=nums[l]
            r=l
            while nums[r]!=0 and r<n-1:
                r+=1
                tmp*=nums[r]
                if tmp>0:
                    res = max(res,r-l+1)
            l=r+1 
        return res
class Solution:
    def getMaxLen(self, nums) -> int:
        
        n,l,r = len(nums),0,0
        res = 0
        while l<n:
            cnt = 0
            prefix = []
            r=l
            while r<n and nums[r]!=0:
                if nums[r]<0:
                    if not prefix:
                        prefix.append(1)
                    else:
                        prefix.append(prefix[-1]+1)
                    cnt+=1
                else:
                    if not prefix:
                        prefix.append(0)
                    else:
                        prefix.append(prefix[-1])
                r+=1
            if cnt%2==0:
                res = max(res,r-l) 
            else:
                r_long = len(prefix)-self.bisect(prefix,2)
                for i in range(l+self.bisect(prefix,2)-1,l-1,-1):
                    if nums[i]>0:
                        r_long +=1
                    else:
                        break
                r_long = max(r_long,self.bisect(prefix,1))
                l_long = self.bisect(prefix,cnt)
                temp = max(r_long,l_long)
                res = max(res,temp)
            if res ==0 and cnt<len(prefix):
                res = max(res,1)
            l=r+1 
        return res

    def bisect(self,prefix,t):
        l,r = 0,len(prefix)
        while l<r:
            mid = (l+r)//2
            if prefix[mid]<t:
                l=mid+1
            else:
                r=mid
        return l
class Solution1:
    def getMaxLen(self, nums) -> int:
        n,l,r = len(nums),0,0
        res = 0
        while l<n:
            tmp=nums[l]
            if nums[l]>0:
                res = max(res,1)
            r=l
            while r<n and nums[r]!=0:
                if nums[r]>0:
                    res = max(res,1)
                tmp*=nums[r]
                if tmp>0:
                    res = max(res,r-l+1)
                r+=1
            tmp = nums[r-1]
            for i in range(r-1,l-1,-1):
                tmp*=nums[i]
                if tmp>0:
                    res = max(res,r-i)
                   
            l=r+1 
        return res
s =Solution()
s.getMaxLen([-16,0,-14,4,-13,-17,-19,-17,-21,-11,12])
[1,-2,-3,4]
[0,1,-2,-3,-4]
[-1,-2,-3,0,1]
[-1,2]
[1,2,3,5,-6,4,0,10]
#对间隔二分,如果当前间隔mid能取到的点数>=m(说明间隔取得小了),则说明答案再mid的右边
# 如果当前间隔mid能取到的点数<m(说明间隔取得大了),则说明答案再mid的左边
class Solution:
    def maxDistance(self, position, m: int) -> int:
        l,r = 0,10**9
        position.sort()
        while l<r:
            mid = (l+r)//2+1
            cnt,last = 1,position[0]
            for i in range(1,len(position)):
                if position[i]-last >=mid:
                    last = position[i]
                    cnt+=1
            if cnt>=m:
                l = mid
            else:
                r=mid-1
        return r
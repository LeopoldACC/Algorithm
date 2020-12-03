class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n = len(intervals)
        l,r = 0,n-1
        while l<r:
            mid = (l+r+1)//2
            if intervals[mid][0]<=newInterval[0]:
                l = mid
            else:
                r = mid-1
        
        # 如果左边> 右边< 在两个中间 [1,3] [6,9] 中间插入[4,5]
        if newInterval[0]>intervals[l][1]:
            if l==n-1 or newInterval[1]<intervals[l+1][0]:
                return intervals[:l+1] + [newInterval] + intervals[l+1:]
            else:
                p = l+1
                while p<n and intervals[p][1]<=newInterval[1]:
                    p+=1
                if p<n and intervals[p][0]<=newInterval[1]:
                    cur_r = intervals[p][1]
                    return intervals[:l+1] + [[newInterval[0],cur_r]] + intervals[p+1:] 
                else:
                    cur_r = max(newInterval[1],intervals[p-1][1])
                    return intervals[:l+1] + [[newInterval[0],cur_r]] + intervals[p:] 
                
        # 如果左边>= 右边<  [2,5] 插入 [3,4]   [1,5] 插入 [0,3]
        elif intervals[l][0]<=newInterval[1]<intervals[l][1]:
            intervals[l][0] = min(intervals[l][0],newInterval[0])
            return intervals
        # [0,0] [1,5]
        # 右边< intervals[l][0]
        elif newInterval[1]<intervals[l][0]:
            return [newInterval]+intervals
        # 其他情况就是 左边> 右边> [1,3] [6,9] 插入[2,5]
        else:
            p = l
            while p<n and intervals[p][1]<=newInterval[1]:
                p+=1
            if p<n and intervals[p][0]<=newInterval[1]:
                cur_r = intervals[p][1]
                return intervals[:l] + [[min(intervals[l][0],newInterval[0]),cur_r]] + intervals[p+1:]
            else:
                cur_r = max(newInterval[1],intervals[p-1][1])
                return intervals[:l] + [[min(intervals[l][0],newInterval[0]),cur_r]] + intervals[p:]
            


s = Solution()
intervals = [[2,7],[8,8],[10,10],[12,13],[16,19]]
newInterval =[9,17]
s.insert(intervals,newInterval)
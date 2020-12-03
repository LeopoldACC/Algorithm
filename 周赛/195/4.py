class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = collections.deque()
        res = float('inf')
        for i in range(len(points)):
            x,y = points[i]
            while q and x-q[0][0]>k:
                q.popleft()
            if q:
                res = max(res,y+q[0][1]+x-q[0][0])
            while q and y-x>(q[-1][1]-q[-1][0]):#当前x一定比q[-1][0]大,所以abs(xi-xj) = x-q[-1][0]  max(yi+yj) = max(y+q[-1][1]) = y+max(q[-1][1]) 
                #就是说对于后面新进的值,我只要 队列中存最大的y-x就行 因为我们+前面的y-前面的x
                q.pop()
            q.append((x,y))            
            
        return res
                    
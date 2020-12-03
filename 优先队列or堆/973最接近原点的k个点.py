class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def calcd(x,y):
            return x**2+y**2
        h=[]
        for i,[x,y] in enumerate(points):
            heapq.heappush(h,[calcd(x,y),x,y])
            # points[i] = [calcd(x,y),x,y]
        points = h
        # heapq.heapify(points)
        res = []
        while K:
            d,x,y = heapq.heappop(points)
            res.append([x,y])
            K-=1
        return res
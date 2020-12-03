#https://www.cnblogs.com/Fantastic-Code/p/9611009.html
#遍历两点距离>2r
import math
class Solution:
    def numPoints(self, points, r):
        def dist2(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        def getCircle(p1, p2):
            mid = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            angle = math.atan((p1[0] - p2[0]) / (p2[1] - p1[1])) if p2[1] - p1[1] else math.pi / 2
            d = math.sqrt(r2 - dist2(p1, mid))
            return [mid[0] + d * math.cos(angle), mid[1] + d * math.sin(angle)]
        
        n = len(points)
        ans = 1
        eps = 1e-6
        r2 = r * r
        for i in range(n):
            for j in range(i + 1):
                if dist2(points[i], points[j]) > 4 * r2:
                    continue
                center = getCircle(points[i], points[j])
                count = 0
                for k in range(n):
                    if dist2(points[k], center) < r2 + eps:
                        count += 1
                ans = max(ans, count)
        return ans
s =Solution()
points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]]
r = 5

ans = s.numPoints(points,r)
print(ans)
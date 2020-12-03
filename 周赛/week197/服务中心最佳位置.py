import math
class Solution:
    def getMinDistSum(self, positions) -> float:
        a1=a2 = len(positions)
        b1,c1 = 0,0
        b2,c2 = 0,0
        for pos in positions:
            b1-=2*pos[0]
            b2-=2*pos[1]
            c1+=pos[0]**2
            c2+=pos[1]**2
        delta1 = math.sqrt(b1*b1-4*a1*c1) if b1*b1-4*a1*c1>0 else 0
        delta2 = math.sqrt(b2*b2-4*a2*c2) if b2*b2-4*a2*c2>0 else 0
        x = (-b1+delta1)/(2*a1)
        y = (-b2+delta2)/(2*a2)
        res = 0.0
        for pos in positions:
            res+= math.sqrt((x-pos[0])**2+(y-pos[1])**2)
        return res
class Solution(object):

    def getMinDistSum(self, A):
        n = len(A)
        x = sum(x for x, y in A) * 1.0 / n
        y = sum(y for x, y in A) * 1.0 / n
        step = 11.0
        e = 1.0
        p = 0.99

        def dis(x, y):
            res = 0
            for i, j in A:
                res += ((x - i)**2 + (y - j)**2) ** 0.5
            return res
        d = dis(x, y)

        print x, y, d

        while step > 0.00000001:
            dx, dy = random.random() * 2 - 1.0, random.random() * 2 - 1.0
            dx *= step
            dy *= step
            x2, y2 = x + dx, y + dy
            d2 = dis(x2, y2)
            if d > dis(x2, y2):
                d = d2
                x, y = x2, y2
            # else:
            #     delta = d2 - d

            #     if (2.71828**(-delta / step) > random.random()):
            #         x, y = x2, y2
            step *= 0.97
        return d
s = Solution()
pos = [[0,1],[1,0],[1,2],[2,1]]
s.getMinDistSum(pos)
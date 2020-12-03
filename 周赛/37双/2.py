import random
import math
class Solution:
    import random
    def bestCoordinate(self, towers, radius: int):
        def getsum(x,y):
            res = 0.0
            for t in towers:
                d = math.sqrt((x-t[0])**2+(y-t[1])**2)
                if d<radius:
                    res+=math.floor(t[2] / (1.0 + d))
            return res

        maxi = 0
        res = [0,0]
        for i in range(51):
            for j in range(51):

                cur = getsum(i,j)
                if cur>maxi:
                    maxi = cur
                    res = [i,j]
        return res
towers = [[28,6,30],[23,16,0],[21,42,22],[50,33,34],[14,7,50],[40,31,4],[39,45,17],[46,21,12],[45,36,45],[35,43,43],[29,41,48],[22,27,5],[42,44,45],[10,49,50],[47,43,26],[40,36,25],[10,25,6],[27,30,30],[50,35,20],[11,0,44],[34,29,28]]
r = 12
s = Solution()
print(s.bestCoordinate(towers,r))
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {'N':(0,1),
                      'S':(0,-1),
                      'E':(1,0),
                      'W':(-1,0)}
        x,y = 0,0
        visit = set()##又是一样的问题直接add((0,0))会压缩到1
        visit.add((0,0))
        for ch in path:
            dx,dy = directions[ch]
            x,y = x+dx,y+dy
            if (x,y) in visit:
                return True
            visit.add((x,y))
        return False
so = Solution()
path = "NESWW"
so.isPathCrossing(path)
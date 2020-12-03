class Solution:
    def unhappyFriends(self, n: int, preferences, p) -> int:
        def check(x,y,u,v):
            uinx =-1
            yinx =-1

            xinu =-1
            vinu =-1
            for idx in range(len(preferences[x])):
                if preferences[x][idx]==u:
                    uinx = idx
                if preferences[x][idx]==y:
                    yinx = idx
            for idx in range(len(preferences[u])):
                if preferences[u][idx]==x:
                    uinx = idx
                if preferences[u][idx]==v:
                    yinx = idx
            return uinx<yinx and xinu<vinu
        n = len(p)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                if check(p[i][0],p[i][1],p[j][0],p[j][1]):
                    res+=2
        return res
s =Solution()
n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]
s.unhappyFriends(n,preferences,pairs)
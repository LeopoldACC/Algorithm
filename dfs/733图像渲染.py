class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        ori = image[sr][sc]
        m,n = len(image),len(image[0])
        visit = set()
        def dfs(x,y):
            visit.add((x,y))
            image[x][y] = newColor
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and image[nx][ny]==ori and (nx,ny) not in visit:
                    dfs(nx,ny)
        dfs(sr,sc)
        return image

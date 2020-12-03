class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        q = collections.deque([(sr,sc)])
        ori = image[sr][sc]
        m,n = len(image),len(image[0])
        visit = set()
        while q:
            x,y = q.popleft()
            image[x][y] = newColor
            visit.add((x,y))
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and image[nx][ny] == ori and (nx,ny) not in visit:
                    q.append((nx,ny))
        return image

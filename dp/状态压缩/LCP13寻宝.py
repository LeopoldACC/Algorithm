import collections
class Solution:
    def minimalSteps(self, maze) -> int:
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        m,n = len(maze),len(maze[0])
        keys,locks = [],[]
        for i in range(m):
            for j in range(n):
                if maze[i][j]=='M':#机关
                    locks.append([i,j])
                if maze[i][j]=='O':#石堆
                    keys.append([i,j])
                if maze[i][j]=='S':
                    si = i
                    sj = j
                if maze[i][j]=='T':
                    ti = i
                    tj = j
        locks = [[si,sj]] + locks#把起点也作为锁 错因:start不是0 0而是si,sj
        # print(locks)
        # print(keys)
        nk,nl = len(keys),len(locks)
        tdist = [[float('inf')] * n for _ in range(m)]#终点和各点距离
        kdist = [[[float('inf')] * n for _ in range(m)] for _ in range(nk)]#石堆和各点距离
        # print(kdist)
        def bfs(i,j,dist):
            q = collections.deque([])
            visit = [[False] * n for _ in range(m)]
            q.append((i,j))
            dist[i][j] = 0
            visit[i][j] = True
            while q:
                x,y = q.popleft()
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if nx<0 or nx>=m or ny<0 or ny>=n or visit[nx][ny] or maze[nx][ny]=='#':
                        continue
                    dist[nx][ny] = dist[x][y]+1
                    visit[nx][ny] = True
                    q.append((nx,ny))
        for i in range(nk):
            bfs(keys[i][0],keys[i][1],kdist[i])
        bfs(ti,tj,tdist)

        print(kdist)
        ldist = [[float('inf')] * nl for _ in range(nl)]
        for i in range(nl):
            i1,j1 = locks[i][0],locks[i][1]#第i把锁的坐标
            for j in range(nl):
                if i==j: continue
                i2,j2 = locks[j][0],locks[j][1]#第j把锁的坐标
                for k in range(nk):#遍历k把钥匙与第i把及与第j把锁的距离的和的最小值
                    ldist[i][j] = min(ldist[i][j],kdist[k][i1][j1] + kdist[k][i2][j2])
        #dp[cur][state] 表示在第cur个锁，目前开锁状态是state时最小距离和
        dp = [[float('inf')] *(1 << nl) for _ in range(nl)]
        dp[0][1] = 0#第0把锁也就是起点打开时 初始化为0
        for state in range(1,1<<nl):#对2^nl种 nl个锁开与不开的状态进行遍历
            for cur in range(nl):#对nl个锁进行遍历
                if dp[cur][state]==float('inf'): continue#如果当前状态当前锁没有从上一次遍历中到达
                #下一步要打开的锁
                for i in range(1,nl):
                    # 目标锁已经被打开 所以我们继续看下一把锁
                    if state & (1 << i): continue
                    # 目标锁未被打开 则把目标锁打开 
                    ne = state+(1 << i)#则下一个状态是把目标锁打开
                    #ldist[cur][i]存的是从当前锁 去最近的key拿钥匙再去i开锁的距离
                    dp[i][ne] = min(dp[i][ne],dp[cur][state] + ldist[cur][i])
        # 出发去终点前的状态，应当是处于某一机关处，同时所有机关均已打开。
        # 遍历 每个锁是开锁顺序中最后一个开的状态，取最小距离和。
        ans = float('inf')
        for i in range(nl):
            ans = min(ans,dp[i][(1<<nl)-1]+tdist[locks[i][0]][locks[i][1]])
        return ans if ans!=float('inf') else -1
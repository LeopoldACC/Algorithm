class Solution:
    def minSwaps(self, grid) -> int:
        n = len(grid)
        dic = {i:[] for i in range(n)}
        for i in range(n):
            j = n-1
            cnt = 0
            while grid[i][j]==0:
                cnt+=1
                j-=1
            dic[cnt].append(i)#从低行往高行append
        prefix_sum = 0    
        for i in range(n-1,0,-1):
            prefix_sum+=len(dic[i])
            if prefix_sum<n-i:
                return -1
        for i in range(n):
            col = n-1-i#每一行需要的列数
            mini_cost = 201
            for j in range(col,n):
                if len(dic[j])>0:

class Solution:#正确答案
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        order = [0]*n
        for i in range(n):
            j = n-1
            while j>0 and grid[i][j]==0:
                j-=1
            order[i] = j
        
        res = 0
        for i in range(n):
            j = i
            while j<n and order[j]>i:
                j+=1
            if j==n:
                return -1
            res+=j-i
            for k in range(j,i,-1):
                order[k] = order[k-1]
        
        return res


s = Solution()
grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
s.minSwaps(grid)              
            
            
        
                
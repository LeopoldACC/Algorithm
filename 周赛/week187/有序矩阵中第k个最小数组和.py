class Solution0:###和不知道怎么最小，heapq
    def kthSmallest(self, mat, k):
        m,n = len(mat),len(mat[0])
        path = [mat[i][0] for i in range(m)]
        res = sum(path)
        
        ind = [0]*m
        for j in range(n-1,0,-1):
            for i in range(m):
                mat[i][j] -=mat[i][j-1]
            
        
        while th<k:
            pick_row = 0
            for row,index in enumerate(ind):
                if index+1>=n:
                    continue
                pick_row = row if mat[row][index+1]<=mat[pick_row][ind[pick_row]] else pick_row
            ind[pick_row]+=1
            res += mat[pick_row][ind[pick_row]]
            th+=1
        return res
import bisect
class Solution1:
    def kthSmallest(self, mat, k):
        A = []
        for l in mat:
            if not A:
                for x in l: A.append(x)
            else:
                B = []
                for x in l:
                    for y in A:
                        bisect.insort(B, x+y)
                A = B  
            if len(A)>k: A = A[0:k]
        return A[-1]
class Solution2:
    def kthSmallest(self, mat, k):
        from queue import PriorityQueue
        q = PriorityQueue()
        s = 0
        n, m = len(mat), len(mat[0])
        now = [0] * n
        for i in range(n):
            s += mat[i][0]
        q.put([s, now], block=False)
        ss = set()
        ss.add(tuple(now))
        for i in range(k - 1):
            rec = q.get(block=False)
            for j in range(n):
                if rec[1][j] == m - 1:
                    continue
                tmp = [x for x in rec[1]]
                tmp[j] += 1
                xx = tuple(tmp)
                if xx not in ss:
                    ss.add(xx)
                    s = rec[0] - mat[j][rec[1][j]] + mat[j][tmp[j]]
                    q.put([s, tmp], block=False)
        rec = q.get(block=False)
        return rec[0]
import heapq

class Solution3:
    def kthSmallest(self, mat, k):
        m, n = len(mat), len(mat[0])
        # 初始化指针
        pointers = [0] * m 
        # 初始化heap
        heap = []
        curr_sum = 0
        for i in range(m):
            curr_sum += mat[i][0]
        heapq.heappush(heap, [curr_sum, tuple(pointers)])
        # 初始化seen
        seen = set()
        seen.add(tuple(pointers))
        # 执行k次
        for _ in range(k):
            # 从堆中pop出curr_sum(最小数组和)和pointers(指针数组)
            curr_sum, pointers = heapq.heappop(heap)
            # 每个指针轮流后移一位，将new_sum(新的数组和)和new_pointers(新的指针数组)push入堆
            for i, j in enumerate(pointers):#数组index i 对应行数，数组第i项值对应列数
                if j < n - 1:
                    new_pointers = list(pointers)
                    new_pointers[i] = j + 1
                    new_pointers = tuple(new_pointers)
                    if new_pointers not in seen:
                        new_sum = curr_sum + mat[i][j + 1]- mat[i][j]
                        heapq.heappush(heap, [new_sum, new_pointers])
                        seen.add(new_pointers)
        return curr_sum        
s = Solution3()
mat = [[1,3,11],[2,4,6]]
k = 5
ans = s.kthSmallest(mat,k)
print(ans)
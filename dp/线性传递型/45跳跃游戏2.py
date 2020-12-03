#O(n^2)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        f = [n]*n
        f[0]=0
        for i in range(n):
            for j in range(1,nums[i]+1):
                if i+j>n-1:
                    return f[n-1]
                f[i+j] = min(f[i+j],f[i]+1)
        return f[n-1] 
#dp+贪心 O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        f = [n]*n
        f[0] = 0
        last = 0
        for i in range(n):
            while last<n and last+nums[last]<i:
                last+=1
            f[i] = min(f[i],f[last]+1)
        return f[n-1] 
#单调(因为f[i+1]>=f[i]的单调性)队列 dp
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0]*n
        f[0] = 0
        q = collections.deque([])
        q.append(0)
        for i in range(1,n):
            while q and nums[q[0]]+q[0]<i:
                q.popleft()
            if q:
                f[i] = f[q[0]]+1
            while q and f[i]<f[q[0]]:#维护队列单调性 如果当前<队尾
                q.pop()
            q.append(i)
        return f[n-1] 
nums = [2,3,1,1,4]
so = Solution()
so.jump(nums)
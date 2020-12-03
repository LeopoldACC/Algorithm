class Solution1:
    def minOperations(self, nums, x: int) -> int:
        n = len(nums)
        nums = nums+nums
        s = [0]+nums[:]
        for i in range(1,len(nums)+1):
            s[i]+=s[i-1]
        def find(lens):
            # 左边取k个 右边取lens-k个
            mini = float('inf')
            for start in range(n-lens,n+1):
                tmp = s[start+lens]-s[start]
                mini = min(mini,tmp)
                # if tmp==x:return True
            if mini>x:
                return True
            return False
        def check(lens):
            # 左边取k个 右边取lens-k个
            for start in range(n-lens,n+1):
                tmp = s[start+lens]-s[start]
                if tmp==x:return True
            return False
        l,r = 0,n
        heli = []
        while l<r:
            mid = (l+r)//2
            if check(mid):
                heli.append(mid)
            if find(mid):
                r = mid
            else:
                l = mid+1
        for i in range(l+1):
            if check(i):
                return i
        return min(heli) if heli else -1
class Solution:
    def minOperations(self, nums, x: int) -> int:
        import collections
        n = len(nums)
        nums = nums+nums
        s = [0]+nums[:]
        for i in range(1,len(nums)+1):
            s[i]+=s[i-1]
        q = collections.deque([])
        q.append(0)
        res = n+1
        for i in range(1,2*n):
            while q and s[i]-s[q[0]]>x:
                q.popleft()
            if q and s[i]-s[q[0]]==x:
                res = min(res,i-q[0])
            q.append(i)
        return res if res!=n+1 else -1
so = Solution()
nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
x =134365
res = so.minOperations(nums,x)
print(res)
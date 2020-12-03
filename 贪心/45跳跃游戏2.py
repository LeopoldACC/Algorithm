class Solution0:#O(n^2)
    def jump(self, nums) -> int:
        n = len(nums)
        st = [False]*n
        f = [n]*n
        st[0]=True
        f[0] = 0
        for i in range(n):
            if st[i]:
                for j in range(i+1,min(i+nums[i]+1,n)):
                    st[j]=True
                    f[j] = min(f[j],f[i]+1)
        return f[n-1]
class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

nums = [2,3,1,1,4]
so = Solution()
so.jump(nums)
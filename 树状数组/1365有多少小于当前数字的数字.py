class Solution:
    def lowbit(self,x):
        return x&(-x)
    def get(self,x,tr):
        res = 0
        while x>0:
            res+=tr[x]
            x-=self.lowbit(x)
        return res
        
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        res = [0]*n
        tr = [0]*510
        maxn = max(nums)+1
        for idx,x in enumerate(nums):
            x = x+1
            while x<=maxn:
                tr[x]+=1
                x+=self.lowbit(x)
        for i in range(n):
            res[i] = self.get(nums[i]-1,tr)
        return res
s = Solution()
nums = [5,0,10,0,10,6]
s.smallerNumbersThanCurrent(nums)
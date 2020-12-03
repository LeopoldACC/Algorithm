class Solution:
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if n<2:return 0
        
        maxi,mini = max(nums),min(nums)
        seq = max(1,(maxi-mini)//(n-1))
        buc = [[] for _ in range((maxi-mini)//seq+1)]
        for i in range(n):
            loc = (nums[i]-mini)//seq
            buc[loc].append(nums[i])

        pre_max = float('inf')
        res = 0
        for i in range(len(buc)):
            if buc[i] and pre_max!=float('inf'):
                res = max(res,min(buc[i])-pre_max)
            if buc[i]:
                pre_max = max(buc[i])
        return res
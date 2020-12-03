
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False
        def dfs(nums):
            if len(nums)==1: 
                return abs(nums[0]-24)<1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i!=j:
                        nextnums = [nums[k] for k in range(len(nums)) if i!=k!=j]
                        ## 等价于i!=k and j!=k 
                        ## 不能是 k!=i!=j  这样就没有约束k!=j了
                        if dfs(nextnums+[nums[i]+nums[j]]):
                            return True
                        if dfs(nextnums+[nums[i]*nums[j]]):
                            return True
                        if dfs(nextnums+[nums[i]-nums[j]]):
                            return True
                        if nums[j]!=0 and dfs(nextnums+[nums[i]/nums[j]]):
                            return True
            return False
        return dfs(nums)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        vis = set()
        nums.sort()
        def dfs(start,path):
            if len(path)==n:
                res.append(path[:])
            for i in range(n):
                if i>0 and nums[i]==nums[i-1] and i-1 in vis:
                    continue
                if i in vis:
                    continue
                vis.add(i)
                path.append(nums[i])
                dfs(i+1,path)
                vis.remove(i)
                path.pop()
        dfs(0,[])
        return res
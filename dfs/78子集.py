class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(start,path):
            if start>n: return
            res.append(path[:])
            for i in range(start,n):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
        dfs(0,[])
        return res
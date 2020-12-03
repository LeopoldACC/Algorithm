class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        path,res=[],[]
        def dfs(nums,path):
            if len(path)==n:
                res.append(path[:])
                return
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(nums[:i]+nums[i+1:],path)
                path.pop()
        dfs(nums,path)
        return res

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, hash_set, path, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not nums[i] in hash_set:
                    hash_set.add(nums[i])
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, hash_set, path, res)
                    path.pop()
                    hash_set.remove(nums[i])

        size = len(nums)
        if size == 0:
            return []
        res = []
        path = []
        hash_set = set()
        dfs(nums, size, 0, hash_set, path, res)
        return res

class Solution:
    def partition(self, s: str):
        res = []
        
        def dfs(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], tmp + [s[:i]])
        dfs(s, [])
        return res
so = Solution()
s = "aab"
so.partition(s)
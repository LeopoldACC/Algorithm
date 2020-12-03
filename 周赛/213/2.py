class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.res=0
        def dfs(path):
            if len(path)==n:
                self.res+=1
                return 
            for ch in ["a","e","i","o","u"]:
                if not path or ord(path[-1])<=ord(ch): 
                    dfs(path+ch)
        dfs('')
        return self.res
s = Solution()
res = s.countVowelStrings(50)
print(res)
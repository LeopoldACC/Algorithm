class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        f = [False]*(n+1)
        f[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        if not f[n]:
            return [] 
        res = []
        def dfs(s,path):
            if not s:
                res.append(' '.join(path))
                return
            for i in range(1,len(s)+1):
                if s[:i] in wordDict:
                    dfs(s[i:],path+[s[:i]])
        dfs(s,[])
        return res
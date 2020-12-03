class Solution:
    def countAndSay(self, n: int) -> str:
        def dfs(i,ch):
            if i==0:
                return ch
            l,r=0,0
            res = []
            while r<len(ch):
                while r<len(ch) and ch[l]==ch[r]:
                    r+=1
                res.append(str(r-l)+ch[l])
                l=r
            print(res)
            return dfs(i-1,''.join(res))
        return dfs(n,'1')
s = Solution()
s.countAndSay(3)
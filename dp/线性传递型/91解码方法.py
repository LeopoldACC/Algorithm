class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [0]*(n+1)
        f[0]=1
        for i in range(1,n+1):
            if 1<=int(s[i-1])<=9:
                f[i]+=f[i-1]
            if i>=2 and 10<=int(s[i-2]+s[i-1])<=26:
                f[i]+=f[i-2]
        return f[-1]

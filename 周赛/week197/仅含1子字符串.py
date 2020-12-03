class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        mod = 1000000007
        n = len(s)
        l,r = 0,0
        while l<n:
            while l<n and s[l]=='0':
                l+=1
            r = l
            while r<n and s[r]!='0':
                r+=1
            tmp_length = r-l
            res=(res+((1+tmp_length)*tmp_length//2)%mod)%mod
            l = r+1
        return res
    
s = Solution()
test = ["0110111","101","111111","000"]
for ch in test:
    res = s.numSub(ch)
    print(res)
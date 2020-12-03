class Solution:
    def sortString(self, s: str) -> str:
        cnt = [0]*26
        res = ""
        n = len(s)
        for ch in s:
            cnt[ord(ch)-ord('a')]+=1
        up = True
        while n:
            if up:
                cntup = 0
                for j in range(26):
                    if cnt[j]:
                        res+=chr(j+ord('a'))
                        cnt[j]-=1
                        cntup+=1
                        n-=1
                up = False
            else:
                cntdown = 0
                for j in range(25,-1,-1):
                    if cnt[j]:
                        res+=chr(j+ord('a'))
                        cnt[j]-=1
                        cntdown+=1
                        n-=1
                up = True
        return res
#审题很重要 是加到不能加为止 而不是只有三个abccba 这种 如果是abcdef这种连续满足的就一直加
so = Solution()
so.sortString("gtqxozxzrssrzxzoxqtg")
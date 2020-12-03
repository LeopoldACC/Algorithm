class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ''
        lens = n-1
        while n:
            if lens*26>=k:
                res+='a'
                k-=1
                lens-=1
            else:
                numsz = k//26
                ne = str(k%26+ord('a'))
                res+=ne
                res+='z'*numsz
                break
        return res
so = Solution()
so.getSmallestString(3,27)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        n = len(s)
        for i in range(0,numRows):
            if i==0 or i==numRows-1:
                for j in range(i,n,2*(numRows-1)):
                    res+=s[j]
            else:
                j,k = i,2*(numRows-1)-i
                while j<n or k<n:
                    if j<n:
                        res+=s[j]
                        j+=2*(numRows-1)
                    if k<n:
                        res+=s[k]
                        k+=2*(numRows-1)
        return res
so = Solution()
s = "LEETCODEISHIRING"
numRows = 3
so.convert(s,numRows)
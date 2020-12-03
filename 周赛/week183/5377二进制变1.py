class Solution:
    def numSteps(self, s: str) -> int:
        s = int(s,2)
        res = 0
        while s !=1:
            if s%2==1:
                s+=1
                res+=1
            else:
                s//=2
                res+=1
        return res
s =Solution()
print(s.numSteps("1101"))
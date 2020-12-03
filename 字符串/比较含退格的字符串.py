class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = S
        t = T
        i=0
        while s and i<len(s):
            if s[i]=="#":
                if i==0:
                    s = s[1:]
                    continue
                s = s[:i-1]+s[i+1:]
                i-=2 if i>1 else 1
            else:
                i+=1
        i=0
        while t and i<len(t):
            if t[i]=="#":
                if i==0:
                    t = t[1:]
                    continue
                t = t[:i-1]+t[i+1:]
                i-=2 if i>1 else 1
            else:
                i+=1

        return s==t
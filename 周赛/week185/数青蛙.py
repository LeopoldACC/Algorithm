class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c,r,o,a,k = 0,0,0,0,0
        res = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                if k>0:
                    k-=1    
                else:
                    res+=1
                c+=1
            if ch == 'r':
                c-=1
                r+=1
            if ch == 'o':
                r-=1
                o+=1
            if ch == 'a':
                o-=1
                a+=1
            if ch == 'k':
                a-=1
                k+=1
            if c<0 or r<0 or o<0 or a<0:
                return -1

        if c!=0 or r!=0 or o!=0 or a!=0:
            return -1
        return res
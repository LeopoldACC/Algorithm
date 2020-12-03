class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n = len(a),len(b)
        if m<n:
            a,b = b,a
            m,n = n,m
        a,b = a[::-1],b[::-1]
        res = ""
        fun = {0:0,1:1,2:0,3:1}
        pref = {0:0,1:0,2:1,3:1}
        pre = 0
        for i in range(m+1):
            
            tmp = 0
            if i<n:
                tmp = fun[int(a[i])+int(b[i])+pre] 
                pre = pref[int(a[i])+int(b[i])+pre]
                res += str(tmp)
            elif i<m:
                tmp = fun[int(a[i])+pre]
                pre = pref[int(a[i])+pre]
                res += str(tmp)
            else:
                tmp = pre
                res +=str(tmp) if tmp>0 else ""
        return res[::-1]
a = "1010"
b = "1011"
so = Solution()
so.addBinary(a,b)
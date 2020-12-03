class Solution:
    def minCost(self, s: str, cost) -> int:
        n = len(s)
        pre_s = [0]*(n+1)
        for i in range(1,n+1):
            pre_s[i]=pre_s[i-1]+cost[i-1]
            
        l,r = 0,0
        qujian = []
        while l<n:
            r = l+1
            maxi = cost[l]
            tag = False
            while r<n and s[r]==s[l]:
                maxi = max(maxi,cost[r])
                r+=1
                tag = True
            if tag:
                qujian.append([l+1,r,maxi])
            l = r    
        res = 0
        for i in range(len(qujian)):
            l,r,maxi = qujian[i][0],qujian[i][1],qujian[i][2]
            sums = pre_s[r]-pre_s[l-1]
            res+=sums-maxi
        return res
so = Solution()
s = "aabaa"
cost = [1,2,3,4,1]
so.minCost(s,cost)
        
            
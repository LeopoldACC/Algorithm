class Solution:
    def mostVisited(self, n: int, rounds):
        N=110
        cnt = [0]*N 
        m = len(rounds)
        cnt[rounds[0]]=1
        for i in range(1,m):
            if rounds[i]>rounds[i-1]:
                for j in range(rounds[i-1]+1,rounds[i]+1):
                    cnt[j]+=1
            else:
                for j in range(rounds[i-1]+1,n+1):
                    cnt[j]+=1
                for j in range(1,rounds[i]+1):
                    cnt[j]+=1

        maxi = max(cnt)
        res = []
        for i in range(1,n+1):
            if cnt[i]==maxi:
                res.append(i)
        return res
        
    
    
        
    
s = Solution()
n = 4
r = [1,3,1,2]
s.mostVisited(n,r)
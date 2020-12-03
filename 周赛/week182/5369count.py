class Solution:###没加break没通过,加了break才通过
    def numTeams(self, rating):
        self.res=0
        self.dfs(rating,[])
        return self.res
    
    def dfs(self,rating,path):
        
        if self.is_valid(path):
            self.res += 1
            return
        for i in range(len(rating)):
            if len(path)<3:
                path.append(rating[i])
                self.dfs(rating[i+1:],path)
                path.pop()
            else:###len(path)==3 那么就可以回到上一层了 而不需要继续遍历 
                break
    def is_valid(self,p):
        if len(p)==3:
            return p[0]>p[1]>p[2] or p[0]<p[1]<p[2]
class Solution1:###暴力就能通过
    def numTeams(self, rating):
        res = 0
        n = len(rating)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if rating[i]>rating[j]>rating[k] or rating[i]<rating[j]<rating[k]:
                        res+=1
        return res
s = Solution()
rating = [2,5,3,4,1]
print(s.numTeams(rating))
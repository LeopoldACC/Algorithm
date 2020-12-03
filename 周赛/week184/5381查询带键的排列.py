class Solution:
    def processQueries(self, queries, m):
        P = [i for i in range(1,m+1)]
        index = {n+1:n for n in range(m)}
        res = []
        for i in range(len(queries)):
            pos = index[queries[i]]
            res.append(pos)
            P[1:pos+1] = P[0:pos]
            for j in range(pos,0,-1):
                index[P[j]]+=1
            P[0] = queries[i]
            index[queries[i]] = 0
            
        return res
s =Solution()
queries = [3,1,2,1] 
m = 5
print(s.processQueries(queries,m))
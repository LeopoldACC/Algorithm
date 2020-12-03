import collections
class Solution:
    def findItinerary(self, tickets):
        n = len(tickets)
        nex = {}
        indegree = {}
        incount = {}
        outcount = {}
        for cur,ne in tickets:
            nex[cur] = nex.get(cur,[])
            nex[cur].append(ne)
            nex[ne] = nex.get(ne,[])
            indegree[cur] = indegree.get(cur,{})
            indegree[cur][ne] = indegree[cur].get(ne,0)+1    
            indegree[ne] = indegree.get(ne,{})  
            indegree[ne][cur] = indegree[ne].get(cur,0)
            incount[cur] = incount.get(cur,0)
            incount[ne] = incount.get(ne,0)+1
            outcount[cur] = outcount.get(cur,0)+1
            outcount[ne] = outcount.get(ne,0)
        final = ''
        for key in nex:
            nex[key].sort()
            # for ne in nex[key]:
            #     if indegree[key][ne]-indegree[ne][key]==1:
            #         final = ne
            #     if indegree[key][ne]-indegree[ne][key]==-1:
            #         final = key
        q = collections.deque(['JFK'])
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            if len(res)==14:
                x=1
            for ne in nex[node]:
                # if ne==final and len(res)!=n and incount[ne]==1:#回路的ne节点只剩1个入度的时候就不妨问它了
                if incount[ne]==1 and outcount[ne]==0 and len(res)!=n and incount[ne]==1:#回路的ne节点只剩1个入度的时候就不妨问它了
                    continue
                if indegree[node][ne]>0:
                    indegree[node][ne]-=1
                    incount[ne]-=1
                    outcount[node]-=1
                    q.append(ne)
                    break
        return res

s =Solution()
s.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])
import collections
class SolutionBFS:
    ##不能用BFS 因为我们需要知道一个支路走到底之后能不能回  而BFS只能知道 支路的第一个节点能不能回
    ## 能回有两种方式
    ## 1 回环
    ## 2 返回
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

import collections
import heapq
class Solution:
    def findItinerary(self, tickets):
        n = len(tickets)
        def dfs(cur):
            while(ne[cur]):
                tmp = heapq.heappop(ne[cur])
                dfs(tmp)
            res.append(cur)
        ne = collections.defaultdict(list)
        for node,nex in tickets:
            ne[node].append(nex)
        for key in ne:
            heapq.heapify(ne[key])#堆保证字典序
        res = []
        dfs('JFK')
        return res[::-1]
s =Solution()
# [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# [["JFK","ATL"],["ORD","PHL"],["JFK","ORD"],["PHX","LAX"],["LAX","JFK"],["PHL","ATL"],["ATL","PHX"]]
# [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])

priority_queue<string, vector<string>, std::greater<string>> 才是pop小顶堆
class Solution {
public:
    unordered_map<string, priority_queue<string, vector<string>, std::greater<string>>> ne;
    vector<string> res;
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for(int i=0;i<tickets.size();i++)
        {
            ne[tickets[i][0]].emplace(tickets[i][1]);
        }
        dfs("JFK");
        reverse(res.begin(),res.end());
        return res;
    }
    void dfs(string cur)
    {
        while(ne[cur].size())
        {
            string tmp = ne[cur].top();
            ne[cur].pop();
            dfs(tmp);
        }
        res.push_back(cur);
    }
};
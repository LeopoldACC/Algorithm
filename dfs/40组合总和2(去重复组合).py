class Solution:
    def combinationSum2(self, candidates, target: int):
        def dfs(start,path,target):
            if target==0:
                res.append(path[:])
                return
            if target<0:
                return
            for i in range(start,len(candidates)):
                if i in vis:
                    continue
                #啥意思呢 就是说 我排完序之后[1,1,2,5,6,7,10] 相同的1在一起了 那么
                #只要我如果根节点从第二个1开始 则就不考虑它和后面的数去组合了
                #因为第一个1 和 2,5 || 7已经组合过一次了
                #但我还需要 1 1 6 这样的数中不同层的相同的数
                # 所以限制i>start才有这样的限制,因为i>start代表相同层(在这个例子里是根节点)的选择不能相同
                if i>start and candidates[i-1]==candidates[i]:
                    continue
                path.append(candidates[i])
                vis.add(i)
                dfs(i+1,path,target-candidates[i])
                vis.remove(i)
                path.pop()
        vis =set()
        res = []
        candidates.sort()
        dfs(0,[],target)
        return res
s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
s.combinationSum2(candidates,target)

class Solution {
public:
    unordered_set<int> vis;
    vector<vector<int>> res;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        dfs(0,{},target,candidates);
        return res;
    }
    void dfs(int start,vector<int> path,int target,vector<int>& candidates)
    {
        if(target==0)
        {
            res.push_back(path);
            return;
        }
        if(target<0)
        {
            return;
        }
        for(int i=start;i<candidates.size();i++)
        {
            if(vis.find(i)!=vis.end()) continue;
            if(i>start && candidates[i]==candidates[i-1])continue;
            path.push_back(candidates[i]);
            vis.insert(i);
            dfs(i+1,path,target-candidates[i],candidates);
            vis.erase(i);
            path.pop_back();
        }
    }
};
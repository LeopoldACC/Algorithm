class Solution:
    def combinationSum(self, candidates, target: int):
        def dfs(start,path,target):
            if target==0:
                res.append(path[:])
                return
            if target<0:
                return
            for i in range(start,n):
                path.append(candidates[i])
                dfs(i,path,target-candidates[i])
                path.pop()
        res = []
        n = len(candidates)
        dfs(0,[],target)
        return res

class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        dfs(0,candidates,{},target);
        return res;
    }
    void dfs(int start,vector<int>& candidates,vector<int> path,int target)
    {
        if(target==0)
        {
            res.push_back(path);
            return;
        }
        if(target<0) return;
        for(int i=start;i<candidates.size();i++)
        {
            path.push_back(candidates[i]);
            dfs(i,candidates,path,target-candidates[i]);
            path.pop_back();
        }
    }
};

#二刷
class Solution:
    def combinationSum(self, can, target: int) -> List[List[int]]:
        n = len(can)
        res = []
        def dfs(path,t,start):
            if t<0:
                return 
            if t==0:
                res.append(path[:])
                return
            for i in range(start,n):
                path.append(can[i])
                dfs(path,t-can[i],i)
                path.pop()
        dfs([],target,0)
        return res
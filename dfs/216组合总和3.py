class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start,n,path):
            if n==0 and len(path)==k:
                res.append(path[:])
                return
            if n<0 or len(path)>k:
                return
            for i in range(start,10):
                if not vis[i]:
                    path.append(i)
                    vis[i] = True
                    dfs(i+1,n-i,path)
                    vis[i] = False
                    path.pop()
        res = []
        vis = {x:False for x in range(1,10)}
        dfs(1,n,[])
        return res
class Solution {
public:
    unordered_map<int,bool> vis;
    vector<vector<int>> res;
    vector<vector<int>> combinationSum3(int k, int n) {
        for(int i=1;i<10;i++) vis[i] = false;
        dfs(1,k,n,{});
        return res;
    }
    void dfs(int start,int k,int n,vector<int> path)
    {
        if(n==0 && path.size()==k)
        {
            res.push_back(path);
            return;
        }
        if(n<0) return;
        for(int i=start;i<10;i++)
        {
            if(!vis[i])
            {
                path.push_back(i);
                vis[i] = true;
                dfs(i+1,k,n-i,path);
                vis[i] = false;
                path.pop_back();
            }
        }
    }
};
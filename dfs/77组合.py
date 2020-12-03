class Solution:
    def combine(self, n: int, k: int):
        def dfs(path,start):
            if len(path)==k:
                res.append(path[:])
                return
            for i in range(start,n+1):
                path.append(i)
                dfs(path,i+1)
                path.pop()
        res = []
        dfs([],1)
        return res

so = Solution()
so.combine(4,2)


class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combine(int n, int k) {
        dfs({},1,n,k);
        return res;
    }
    void dfs(vector<int> path,int start,int n,int k)
    {
        if(path.size()==k)
        {
            res.push_back(path);
            return;
        }
        for(int i=start;i<=n;i++)
        {
            path.push_back(i);
            dfs(path,i+1,n,k);
            path.pop_back();
        }
    }
};
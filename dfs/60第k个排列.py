class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(k,used,path):
            if(len(path)==n):
                k-=1
                if not k:
                    self.res=path
            sub_path_cnt = factor[n-used-1]
            for i in range(1,n+1):
                if not st[i]:
                    if sub_path_cnt<k:
                        k-=sub_path_cnt
                        continue
                    st[i] = True
                    dfs(k,used+1,path+str(i))
                    return
        self.res = ""
        st = [False]*10
        factor = [1 for _ in range(10)]
        for i in range(1,10):
            factor[i] = i * factor[i-1]
        dfs(k,0,"")
        return self.res

# const int N=10;
# class Solution {
# public:
#     bool st[N];
#     string res;
#     int idx;
#     int factor[N];
#     string getPermutation(int n, int k) {
#         factor[0]=1;
#         for(int i=1;i<=9;i++) factor[i] = i*factor[i-1];
#         dfs(n,k,0,"");
#         return res;
#     }
#     void dfs(int n,int k,int used,string path)
#     {
#         if(path.size()==n)
#         {
#             idx++;
#             if(k==idx) res = path;
#             return;
#         }
#         for(int i=1;i<=n;i++)
#         {

#             if(!st[i])
#             {
#                 if(idx+factor[n-used-1]<k)
#                 {
#                     idx+=factor[n-used-1];
#                     continue;
#                 }//用到used位 还剩n-used位 的排列,加上当前位 共还剩n-used-1位的全排列(n-used-1)!种 如果+(n-used-1)!<k 就不往下搜了
#                 st[i]=true;
#                 dfs(n,k,used+1,path+to_string(i));
#                 st[i]=false;
#                 return;
#                 //为什么在dfs(i)了之后就不用看了？
#                 //以 1,2,3 k=3为例 
#                 //因为我们已经提前算好了 首先在开始的时候used=0
#                 // 以1开头的剩下的排列有 idx(0)+(n-used-1)! 如果<k
#                 // 则0都不用往下搜了直接去看以2开头的
#                 // 那么我们最终往下搜是以2开头的(因为2!+2!>3)
#                 // 那么答案一定在以2开头的路径的叶子节点上
#                 // 所以我们只要往下搜完了就不用继续去看以3开头的路径了
#                 // 所以可以直接return 了
#             }
#         }
#     }
# };
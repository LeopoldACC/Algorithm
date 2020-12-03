# class Solution:
#     def findLexSmallestString(self, s: str, a: int, b: int) -> str:
#         vis = set()
#         # s1 = "5525"
#         # s2 = "0"
#         # print(s1[len(s)-b:])
#         # print(s1[:b])
#         # print(s1[:b]+s1[len(s)-b:])
#         def gets1():
#             res = s
#             for i in range(1,len(s),2):
#                 tmp = int(s[i])+a if int(s[i])+a<9 else (int(s[i])+a)%10
#                 res = res[:i]+str(tmp)+res[i+1:]
#             return res
#         def gets2():
#             res = s
#             return res[len(s)-b:]+res[:len(s)-b]
#         while int(s) > int(gets1()) or int(s)>int(gets2()):
#             s1 = gets1()
#             s2 = gets2()
#             ne = s1 if int(s1)<int(s2) else s2
#             if int(ne)<int(s):
#                 s = ne
#         return s
    
# so = Solution()
# # s = "5525"
# # a = 9
# # b = 2
# # s = "74"
# # a = 5
# # b = 1
# s = "43987654"
# a = 7
# b = 3
# so.findLexSmallestString(s,a,b)

# ## 3 最长上升子序列
# class Solution:
#     def bestTeamScore(self, w: List[int], v: List[int]) -> int:
#         n = len(w)
#         V = sum(v)
#         f = [0]*(V+1)
#         for i in range(n):
#             for j in range(V,v[i]-1,-1):
#                 f[j] = max(f[j],f[j-v[i]]+w[i])
#         res = 0
#         for i in range(len(f)):
#             res = max(res,f[i])
#         return res
class Solution:
    def bestTeamScore(self, w, v) -> int:
        ls = [[v[i],w[i]] for i in range(len(w))]
        # print(ls)
        ls.sort()
        # print(ls)
        n = len(ls)
        f = [0]*n
        res = 0
        for i in range(n):
            f[i]=ls[i][1]
            for j in range(i):
                if ls[i][1]>=ls[j][1]:
                    f[i] = max(f[i],f[j]+ls[i][1])
            res = max(res,f[i])
        return res
w = [4,5,6,5]

v = [2,1,2,1]
so = Solution()
so.bestTeamScore(w,v)
###第4题
const int N=10010;
class Solution {
public:
    int f[N];
    int find(int x)
    {   
        if(x!=f[x]) f[x] = find(f[x]);
        return f[x];
    }
    int gcd(int a,int b)
    {
        return b==0?a:gcd(b,a%b);
    }
    
    vector<bool> areConnected(int n, int threshold, vector<vector<int>>& q) 
    {
        // memset(h,-1,sizeof h);
        for(int i=1;i<=n;i++) f[i] = i;
        for(int i=threshold+1;i<=n;i++)
        {
            for(int j=2;j*i<=n;j++)
            {
                    // add(i,j);
                    // add(j,i);
                f[find(i)] = f[find(j*i)]; 
            }
        }
        vector<bool> res(q.size(),false);
        for(int i = 0;i<q.size();i++)
        {
            res[i] = find(q[i][0])==find(q[i][1]);
            // res.push_back(find(t[0])==find(t[1]));
        }   
        return res;
    }
};
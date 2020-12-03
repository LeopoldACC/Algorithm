#include<iostrea>
#include<cstring>
#include<unordered_map>
using namespace std;

const int N=100010;
class Solution {
public:
    
    int f[N],cnt[N],res=-1;
    char string[N];
    unordered_map<int,int> cur_count;//维护实时区间长度是否存在 的字典
    int findLatestStep(vector<int>& arr, int m) {
        int n = arr.size();
        for(int i=1;i<=n;i++)
        {
            f[i]=i;
            cnt[i]=1;//这里只是计算个数 
            string[i] = '0';
        }
        for(int i=0;i<n;i++)
        {
            string[arr[i]] = '1';
            cnt[arr[i]]=1;
            if(string[arr[i]-1]=='1')
            {
                int b = find(arr[i]-1);
                if(cnt[b]==m) res = i;
                cur_count[cnt[b]]--;
                uni(arr[i]-1,arr[i]);
            }
            if(string[arr[i]+1]=='1') 
            {
                int b = find(arr[i]+1);
                if(cnt[b]==m) res = i;
                cur_count[cnt[b]]--;
                uni(arr[i]+1,arr[i]);
            }
            cur_count[cnt[arr[i]]]+=1;
            if(cur_count[m]) res = i+1;
        }
        return res;
    }
    int find(int x)
    {
        if(x!=f[x]) f[x] = find(f[x]);
        return f[x];
    }
    void uni(int x,int y)
    {
        f[find(x)] = find(y);
        cnt[find(y)]+=cnt[find(x)];
    }
};

int main()
{
    Solution s;
    vector<int> op = {1,2,3};
    int m = 2;
    s.findLatestStep(op,m);
    return 0;
}
#include<iostream>
#include<cstring>
#include<algorithm>
#include<string.h>
using namespace std;

const int N=1010;
char s[N];
int f[N][N];
int main()
{
    string str;
    while(cin >> str)
    {
        memset(f,0,sizeof f);
        int n = str.size();
        for(int i=0;i<n;i++) s[i] = str[i];
        int maxi = 0;
        for(int i=n-1;i>=0;i--)
        {
            f[i][i]=1;
            for(int j=i+1;j<n;j++)
            {
                if(s[i]==s[j])
                {
                    if(j-i<=2)
                    {
                        f[i][j] = j-i+1;
                    }
                    else
                    {
                        f[i][j] = f[i+1][j-1]+2;
                    }
                }
                else
                {
                    f[i][j] = max(f[i+1][j],f[i][j-1]);
                }
            }
        }
        int res;
        res = str.size()-f[0][n-1];
        cout << res << '\n';
    }
    return 0;
}
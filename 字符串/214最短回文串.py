const int N=100010;
class Solution {
public:
    int next[N],n;
    char p[N];
    string pre,res;
    string shortestPalindrome(string s) {
        n = s.size();
        string revs = s;
        reverse(revs.begin(),revs.end());
        string cat =s+'#'+revs;
        // cout << cat << endl;
        for(int i=1;i<=2*n+1;i++) p[i] = cat[i-1];
        for(int i=2,j=0;i<=2*n+1;i++)
        {
            while(j && p[i]!=p[j+1]) j=next[j];
            if(p[i]==p[j+1]) j++;
            next[i] = j;
        }
        int len = next[2*n+1];
        // for(int i=1;i<=2*n+1;i++) cout << next[i];
        for(int i=len+1;i<=n;i++) pre+=s[i-1];
        reverse(pre.begin(),pre.end());
        res = pre+s;
        return res;
    }
};
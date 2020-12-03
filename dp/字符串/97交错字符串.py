class Solution_False:#没考虑到顺序 所以要用动规
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cnt1 = {}
        cnt2 = {}
        cnt = {}
        for ch in s1: cnt1[ch] = cnt1.get(ch,0)+1
        for ch in s2: cnt2[ch] = cnt2.get(ch,0)+1
        for ch in s3: cnt[ch] = cnt.get(ch,0)+1

        for ch in cnt:
            if cnt[ch] != cnt1.get(ch,0) +cnt2.get(ch,0):
                return False
        
        return True
class Solution_dp:#没考虑到顺序 所以要用动规dp
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,l = len(s1),len(s2),len(s3)
        if m+n!=l:return False
        dp = [[False] * (n+1) for _ in range(m+1)]#dp[i][j]代表到当前k能匹配上s1的前i个和s2的前j个的组合
        dp[0][0] = True
        for i in range(1,m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1,n+1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or(dp[i-1][j] and s1[i-1]==s3[i+j-1])
        
        return dp[m][n]
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m=s1.size(),n=s2.size(),l=s3.size();
        if (m+n!=l) return false;

        vector<vector<bool> > dp(m+1,vector<bool>(n+1,false));

        dp[0][0] = true;
        for(int i = 1;i<m+1;i++)
            dp[i][0] = dp[i-1][0] && s1[i-1]==s3[i-1];
        for(int i = 1;i<n+1;i++)
            dp[0][i] = dp[0][i-1] && s2[i-1]==s3[i-1];
        for(int i=1;i<m+1;i++)
        {
            for(int j=1;j<n+1;j++)
            {
                dp[i][j] = (dp[i][j-1] && s3[i+j-1]==s2[j-1]) || (dp[i-1][j] && s3[i+j-1]==s1[i-1]);
            }
        }
        return dp[m][n];
    }
};
so =Solution_dp()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
so.isInterleave(s1,s2,s3)
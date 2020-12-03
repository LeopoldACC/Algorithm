class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        f = [[False]*n for _ in range(n)]
        cnt = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[i]==s[j] and (i-j<=2 or f[j+1][i-1]):
                    f[j][i] = True
                    # 说明s[j:i]不用分割 s[:i]分割数=s[:j]分割数+1
                    if j==0:
                        cnt[i] = 0
                    else:
                        cnt[i] = min(cnt[i],cnt[j-1]+1)
        return cnt[n-1]
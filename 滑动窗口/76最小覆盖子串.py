class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        t = Counter(t)
        window = Counter()
        l,r = 0,0
        minlen = float('inf')
        res = ""
        while r<len(s):
            window[s[r]] +=1
            r+=1
            while all(map(lambda x:window[x]>=t[x],t.keys())):##>=写成>
                if r-l<minlen:
                    res = s[l:r]
                    minlen = r-l
                window[s[l]]-=1
                l+=1
        return res
                
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        l,r = 0,0
        cnt = {}
        cnt_t = collections.Counter(t)
        n = len(s)
        res = s
        def check(cnt_s,cnt_t):
            for x in cnt_t:
                if x not in cnt_s:
                    return False
                if cnt_s[x]<cnt_t[x]:
                    return False
            return True
        while r<n:
            while r<n and not check(cnt,cnt_t):
                if s[r] in t:
                    cnt[s[r]] = cnt.get(s[r],0)+1
                r+=1
            while l<r and check(cnt,cnt_t):
                if s[l] in t:
                    cnt[s[l]]-=1
                if r-l<len(res):
                    print(r-l+1)
                res = s[l:r] if r-l<len(res) else res 
                
                l+=1
        return res 
s = Solution()
st = "ADOBECODEBANC"
t = "ABC"
s.minWindow(st,t)
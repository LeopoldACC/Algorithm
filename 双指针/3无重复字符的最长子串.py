class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        n = len(s)
        res = 0
        cnt = {}
        while r<n:
            while r<n and s[r] not in cnt:
                cnt[s[r]] = cnt.get(s[r],0) + 1
                res = max(res,r-l+1)
                r+=1
            cnt[s[r]]+=1
            print(cnt)
            while cnt[s[r]]>1:
                cnt[s[l]]-=1
                l+=1 
        return res
so = Solution()
st = "abcabcbb"
so.lengthOfLongestSubstring(st)
class Solution:
    def commonChars(self, A):
        cnt = {chr(ch):0 for ch in range(ord('a'),ord('z')+1)}
        first = True
        # print(cnt)
        for st in A:
            tmp = {chr(ch):0 for ch in range(ord('a'),ord('z')+1)}
            for ch in st:
                tmp[ch] = tmp.get(ch,0)+1
            if first:
                for ch in tmp:                
                    cnt[ch] = tmp[ch]
                first=False
            else:
                for ch in tmp:
                    cnt[ch] = min(tmp[ch],cnt[ch])
                    
        res = []
        for ch in cnt:
            while cnt[ch]:
                res.append(ch)
                cnt[ch]-=1
        return res    
        
so = Solution()
ls = ["bella","label","roller"]
so.commonChars(ls)
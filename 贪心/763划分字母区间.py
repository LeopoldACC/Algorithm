class Solution:
    def partitionLabels(self, S: str):
        seq = {chr(ord('a')+i):[] for i in range(26)}
        n = len(S)
        for i in range(n):
            if len(seq[S[i]])<2:
                seq[S[i]].append(i)
            else:
                seq[S[i]][1] = i
        
        l,r = 0,0
        
        res = []
        while l<n:
            r=l
            end = seq[S[r]][1] if len(seq[S[r]])==2 else seq[S[r]][0]
            while r<end:
                r+=1
                endc = seq[S[r]][1] if len(seq[S[r]])==2 else seq[S[r]][0]
                end = max(end,endc)
            res.append(end-l+1)
            l = end+1
        return res
s = Solution()
string = "caedbdedda"
s.partitionLabels(string)

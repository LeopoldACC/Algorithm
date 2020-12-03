class Solution:
    def stringMatching(self, words):
        words.sort(key = lambda x:len(x))
        n = len(words)
        if n <2:
            return []
        res = []
        for i in range(n-1):
            for j in range(i+1,n):
                if self.kmp(words[j],words[i]):
                    res.append(words[i])
                    break
        return res                
        
    def kmp(self,string,substring):
        pnext =self.pnext(substring)
        n = len(string)
        m = len(substring)
        i, j = 0, 0
        while (i<n) and (j<m):
            if (string[i]==substring[j]):
                i += 1
                j += 1
            elif (j!=0):
                j = pnext[j-1]
            else:
                i += 1
        if (j == m):
            return True#i-j
        else:
            return False

    def pnext(self,substring):
        index,n = 0,len(substring)
        pnext = [0]*n
        i = 1
        while i < n:
            if (substring[i] == substring[index]):
                pnext[i] = index + 1
                index += 1
                i += 1
            elif (index!=0):
                index = pnext[index-1]
            else:
                pnext[i] = 0
                i += 1
        return pnext
s = Solution()
ls = ["mass","as","hero","superhero"]
print(s.stringMatching(ls))
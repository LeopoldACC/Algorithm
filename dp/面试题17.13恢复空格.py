class dp2:
    def respace(self, dictionary, s: str) -> int:
        dic = set(dictionary)
        n = len(s)
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i-1]+1
            for j in range(i):
                if s[j:i] in dic:
                    dp[i] = min(dp[i],dp[j])
        return dp[-1]

##字典树
class TrieNode:
    def __init__(self):
        self.childs = [0]*26
        self.isWord = False
    
class dpTrie:
    def respace0(self, dictionary, s):
        dic = set(dictionary)
        n = len(s)
        self.root = TrieNode()##根设为空
        self.makeTrie(dictionary)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            dp[i] = n-i
            node = self.root
            for j in range(i,n):
                c = ord(s[j])-ord('a')
                if node.childs[c] ==0:
                    dp[i] = min(dp[i],j-i+1+dp[j+1])
                    break
                if node.childs[c].isWord:
                    dp[i] = min(dp[i],dp[j+1])
                else:
                    dp[i] = min(dp[i],j-i+1+dp[j+1])
                node = node.childs[c]
        return dp[0]
    def makeTrie(self,dictionary):
        for string in dictionary:
            node = self.root
            for k in range(len(string)):
                i = ord(string[k])-ord('a')
                if node.childs[i]==0:
                    node.childs[i] = TrieNode()
                node = node.childs[i]
            node.isWord = True

    def respace1(self, dictionary, s):
        dic = set(dictionary)
        n = len(s)
        self.root = TrieNode()##根设为空
        self.makeTrie_inverse(dictionary)
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i-1]+1
            node = self.root
            for j in range(i,0,-1):
                c = ord(s[j-1])-ord('a')
                if node.childs[c] ==0:
                    break
                if node.childs[c].isWord:
                    dp[i] = min(dp[i],dp[j-1])
                if dp[i]==0:
                    break
                node = node.childs[c]
        return dp[n]

    def makeTrie_inverse(self,dictionary):
        for string in dictionary:
            node = self.root
            for k in range(len(string)-1,-1,-1):
                i = ord(string[k])-ord('a')
                if node.childs[i]==0:
                    node.childs[i] = TrieNode()
                node = node.childs[i]
            node.isWord = True
so = dpTrie()
dic = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
res = so.respace1(dic,sentence)
print(res)
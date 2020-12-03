class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)###len(s) 写成了len(wordDict)
        dp = [False] * (n+1)
        dp[0]=True
        wordDict = set(wordDict)
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
so = Solution()
s = "leetcode"
word = ["leet","code"]
so.wordBreak(s,word)

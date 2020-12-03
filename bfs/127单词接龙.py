class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = collections.deque([])
        q.append([beginWord,1])
        vis = {x:False for x in wordList}
        vis[beginWord] = True
        if endWord not in wordList:
            return 0
        while q:
            for _ in range(len(q)):
                ch,d = q.popleft()
                for i in range(len(ch)):
                    for k in range(26):
                        c = chr(ord('a')+k)
                        ne = ch[:i] + c + ch[i+1:]
                        if ne == endWord:
                            return d+1
                        if ne in vis and not vis[ne]:
                            q.append([ne,d+1])
                            vis[ne] = True
        return 0
s =Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
s.ladderLength(beginWord,endWord,wordList)
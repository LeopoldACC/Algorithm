import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        q = collections.deque([])
        if endWord not in wordList:
            return []
        q.append(beginWord)
        lc = [chr(ord('a')+i) for i in range(26)]
        vis = {ch:False for ch in wordList}
        ne_vis = {ch:False for ch in wordList}
        ne = {}
        res = []
        found = False
        while q:
            for _ in range(len(q)):
                t = q.popleft()
                for i in range(len(t)):
                    for c in lc:
                        nc = t[:i]+c+t[i+1:]
                        if nc not in wordList or vis[nc]==True or nc==t:
                            continue
                        if nc==endWord:
                            if t not in ne:
                                ne[t] = [endWord]
                            else:
                                ne[t].append(endWord)
                            found = True
                            # break
                        ne_vis[nc] = True
                        q.append(nc)
                        vis[nc]=True
                        if t not in ne:
                            ne[t] = [nc]
                        else:
                            ne[t].append(nc)
            for ch in ne_vis:
                vis[ch] = True
                ne_vis[ch]=False
            if found:
                break
            # vis |=ne_vis
            # ne_vis.clear()
        if not found:
            return []
        path = [beginWord]
        self.dfs(beginWord,endWord,ne,path,res)
        return res
    def dfs(self,beginWord,endWord,ne,path,res):
        if beginWord==endWord:
            res.append(path[:])
            return
        if beginWord not in ne:
            return
        ne_c_ls = ne[beginWord]
        for ne_c in ne_c_ls:
            if ne_c not in path:
                path.append(ne_c)
                self.dfs(ne_c,endWord,ne,path,res)
                path.pop()
so = Solution()
b ="red"


e = "tax"
ls = ["ted","tex","red","tax","tad","den","rex","pee"]
so.findLadders(b,e,ls)
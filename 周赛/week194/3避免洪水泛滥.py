import collections
class Solution:
    def avoidFlood(self, rains):
        res = [-1]*len(rains)
        q = collections.deque([])
        dic = {}
        for i,x in enumerate(rains):
            if x==0:
                q.append(i)
                continue
            if x not in dic:
                dic[x] = i
            else:###x有过一次了
                if not q:
                    return []
                else:###有0
                    index = q.popleft()
                    visit = set()
                    while q and index<dic[x]:
                        q.append(index)
                        visit.add(index)
                        index = q.popleft()
                        if index in visit:
                            return []
                    if index>dic[x]:
                        res[index] = x
                        dic[x] = i
                    else:
                        return []
        while q:
            res[q.popleft()] = 1
        return res
so = Solution()
rains = [2,3,0,0,3,1,0,1,0,2,2]
so.avoidFlood(rains)
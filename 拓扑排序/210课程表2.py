
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        indegree = {num:0 for num in range(numCourses)}
        neighbor = {num:[] for num in range(numCourses)}###这里也是每个都要，不然最后一个node在for nex in neighbor(node)时找不到
        for order in prerequisites:
            indegree[order[0]] +=1
            neighbor[order[1]].append(order[0])
        q = collections.deque([])
        for node in indegree:
            if indegree[node]==0:
                q.append(node)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nex in neighbor[node]:###这里nex写成neighbor了
                indegree[nex]-=1
                if indegree[nex]==0:
                    q.append(nex)###这里写成neighbor了
        return res if len(res)==numCourses else []###出现环的时候 res长度达不到numCourses
s = Solution()
a = s.findOrder(3, [[1,0],[1,2],[0,1]])
print(a)
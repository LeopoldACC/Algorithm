class Solution:
    def findOrder(self, numCourses, prerequisites):
        indegree,adjacency = self.get_indegree(prerequisites,numCourses)
        from collections import deque
        q = deque([])
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            pre = q.popleft()
            res.append(pre)
            for cur in adjacency[pre]:
                indegree[cur] -=1
                if not indegree[cur]:
                    q.append(cur)
        return res if len(res)==numCourses else []

    def get_indegree(self,prerequisites,numCourses):
        indegree = {i:0 for i in range(numCourses)}
        adjacency = {i:[] for i in range(numCourses)}
        for cur,pre in prerequisites:
            indegree[cur] += 1
            adjacency[pre].append(cur)###adjacency[cur].append(pre)  adjcency存的是当前节点入的点
        return indegree,adjacency
s =Solution()
n = 4
pre = [[1,0],[2,0],[3,1],[3,2]]
s.findOrder(4,pre)
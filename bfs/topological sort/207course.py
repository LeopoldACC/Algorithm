class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree,adjacency = self.get_indegree(prerequisites,numCourses)
        from collections import deque
        q = deque([])
        for i in range(len(indegree)):
            if indegree[i]==0:###入度为0 说明只i入别人，没有别人入i
                q.append(i)
        while q:
            pre = q.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegree[cur] -= 1
                if indegree[cur] == 0:
                    q.append(cur)        
        
        return numCourses==0
    
    def get_indegree(self,graph,numCourses):
        indegree = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for cur,pre in graph:
            indegree[cur] += 1
            adjacency[pre].append(cur)
        return indegree,adjacency 
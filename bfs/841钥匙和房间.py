import collections
class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        n = len(rooms)
        visit = [False] * n
        visit[0] = True
        q = collections.deque([0])
        while q:
            node = q.popleft()
            for ne in rooms[node]:
                if visit[ne]:
                    continue
                q.append(ne)
                visit[ne]=True
        for i in range(len(visit)):
            if not visit[i]:
                return False
        return True
class Solution_dfs:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = [False] * n
        visit[0] = True
        def dfs(node):
            for ne in rooms[node]:
                if visit[ne]:
                    continue
                visit[ne]=True
                dfs(ne)
                
        dfs(0)
        for i in range(len(visit)):
            if not visit[i]:
                return False
        return True
s = Solution()
rooms = [[1],[2],[3],[]]
s.canVisitAllRooms(rooms)
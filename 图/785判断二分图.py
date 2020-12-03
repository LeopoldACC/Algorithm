class Solution_False:
    def isBipartite(self, graph) -> bool:
        n = len(graph)
        cls = {i:-1 for i in range(n)}
        cls[0]=1
        for i,neighbor in enumerate(graph):
            #为什么不能直接按照给的graph顺序遍历，因为这样的顺序不是按图的邻接点来做的，优先按图的邻接顺序来染色确保染色不冲突
            cls[i]=1 if cls[i]==-1 else cls[i]
            for ne in neighbor:
                if cls[ne]==cls[i]:
                    return False
                if cls[ne]==-1:
                    cls[ne] = 3-cls[i]
        return True

so = Solution()
arr = [[3],[2,4],[1],[0,4],[1,3]]
so.isBipartite(arr)
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        cnt = []

        q = []
        sumh = 0
        for i in range(1,len(heights)):
            if heights[i]>heights[i-1]:
                heapq.heappush(q,heights[i]-heights[i-1])
            if len(q)>ladders:
                sumh+=heapq.heappop(q)
            if sumh>bricks:
                return i-1
        return len(heights)-1
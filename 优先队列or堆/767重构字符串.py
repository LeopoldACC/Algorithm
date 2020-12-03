class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        cnt = collections.Counter(S)
        h = []
        for x in cnt:
            if cnt[x]>(n+1)//2:
                return ""
            h.append([-cnt[x],x])
        heapq.heapify(h)
        res = []
        while len(h)>1:
            _,c1 = heapq.heappop(h)
            _,c2 = heapq.heappop(h)
            res+=[c1,c2]
            cnt[c1]-=1
            cnt[c2]-=1
            if cnt[c1]>0:
                heapq.heappush(h,[-cnt[c1],c1])
            if cnt[c2]>0:
                heapq.heappush(h,[-cnt[c2],c2])
        if len(h)>0:
            _,c = heapq.heappop(h)
            res+=[c]
        return ''.join(res)
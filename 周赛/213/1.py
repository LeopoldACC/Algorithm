class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        st = [False]*len(pieces)
        m = len(pieces)
        tmp = []
        tot = 0
        while m>0:
            for idx,item in enumerate(pieces):
                if st[idx]:
                    continue
                if tmp+item==arr[:len(tmp)+len(item)]:
                    tmp = tmp+item
                    m-=1
                    st[idx]=True
                    break
            tot+=1
            if idx>=len(pieces) and len(tmp)!=len(arr):
                return False
        return len(tmp)==len(arr)
arr = [15,88]
pieces = [[88],[15]]
s = Solution()
s.canFormArray(arr,pieces)
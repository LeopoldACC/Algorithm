class Solution:
    def containsPattern(self, arr, m: int, k: int) -> bool:
        n = len(arr)
        if m*k>n:
            return False
        for l in range(n):
            if l+m*k>n:
                break
            tag = True
            r=l+m*k-1
            for i in range(m):
                for j in range(1,k):
                    tag &= arr[l+i]==arr[l+i+j*m]
                    if not tag:
                        break
            if tag:
                return True
            
        return False
s =Solution()
arr = [1,2,3,1,2]
m = 2
k = 2
s.containsPattern(arr,m,k)
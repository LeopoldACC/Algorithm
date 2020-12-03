class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        for i in range(n-1,-1,-1):
            if i-2<0:
                break
            if A[i-2]+A[i-1]>A[i]:
                return A[i-2]+A[i-1]+A[i]
        return 0
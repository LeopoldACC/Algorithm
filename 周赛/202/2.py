class Solution:
    def minOperations(self, n: int) -> int:
        mid = n
        res = 0
        if n%2!=0:
            for i in range(1,n+1,2):
                print(i)
                res+=n-i
        if n%2==0:
            for i in range(1,n+1,2):
                print(i)
                res+=n-i
        return res
            
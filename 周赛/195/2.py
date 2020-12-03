class Solution:
    def canArrange(self, arr, k: int) -> bool:
        if sum(arr)==0:
            return True
        if sum(arr)%k!=0:
            return False
        return True
        # arr.sort()
        # visit = set()
        # res = set()
        # n=len(arr)
        # num = n//2
        # i=0
        # while (num>0):
        #     while i in visit:
        #         i+=1
        #     j = n-1
        #     while i<j and j in visit:
        #         j-=1
        #     while i<j and (arr[i]+arr[j])%k!=0:
        #         if j in visit:
        #             j-=1
        #             continue
        #         j-=1
        #     if (arr[i]+arr[j])%k==0:
        #         res.add((arr[i],arr[j]))
        #         visit.add(j)
        #         visit.add(i)
        #     i+=1
        #     num-=1
        # for i,j in visit:
        #     print([i,j])
        # return len(visit) == n//2
so = Solution()
arr=[75,5,-5,75,-2,-3,88,10,10,87]
k=85
so.canArrange(arr,k)
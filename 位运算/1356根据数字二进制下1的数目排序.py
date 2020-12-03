class Solution:
    def sortByBits(self, arr):
        def cnt(x):
            res = 0
            while x:
                res+=x%2
                x//=2
            return res
        
        for i,x in enumerate(arr):
            arr[i] = [cnt(x),x]
        arr.sort()
        return [x[1] for x in arr]
s = Solution()
arr = [0,1,2,3,4,5,6,7,8]
s.sortByBits(arr)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l,r = [1]*n,[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                l[i]=l[i-1]+1
        res = l[-1]#最后一个一定是由l决定的--不能初始化为0然后再求
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                r[i]=r[i+1]+1
            res+=max(l[i],r[i])
        return res
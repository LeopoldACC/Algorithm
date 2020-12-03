class Solution:
    def maxNonOverlapping(self, nums, target: int) -> int:
        res = 0
        sums = 0
        visit = set()
        visit.add(0)#对于第一次sums==target的特判 1 1 1 1 1  
        for num in nums:
            sums+=num
            if sums-target in visit:
                visit = set()
                res+=1
                sums=0
            visit.add(sums)
        return res
class Solution:
    def jump(self, nums: List[int]) -> int:
        n,end,rmax = len(nums)-1,0,0
        time = 0
        for i in range(n):
            if i <=rmax:
                rmax = max(rmax,i+nums[i])
                if i==end:
                    time += 1
                    end = rmax
        return time
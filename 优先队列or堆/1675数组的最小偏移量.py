class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        import heapq
        n = len(nums)
        mini = float('inf')
        res = float('inf')
        h = []
        for i in range(n):
            if nums[i]%2==1:
                nums[i]*=2
            heapq.heappush(h,-nums[i])
            mini = min(mini,nums[i])
        while True:
            maxi = -heapq.heappop(h)
            res = min(res,maxi-mini)
            # print(maxi,res)
            if maxi%2==1:
                break
            mini = min(mini,maxi//2)
            heapq.heappush(h,-maxi//2)
        return res

# 作者：仅存老实人
# 链接：https://www.acwing.com/solution/content/26183/
# 来源：AcWing
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
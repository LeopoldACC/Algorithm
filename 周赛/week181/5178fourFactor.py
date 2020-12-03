class Solution:
    def sumFourDivisors(self, nums):
        if len(nums) == 1:
            upper = nums[0]
        else:
            upper = max(*nums)
        number = [0 for i in range(upper+1)]
        cur = [0 for i in range(upper+1)]
        for i in range(1,upper+1):
            for j in range(i,upper+1,i):
                number[j] += 1
                cur[j] += i
        
        ans = 0
        for num in nums:
            if number[num] == 4:
                ans += cur[num]
        
        return ans

s = Solution()
nums = [21,4,7]
s.sumFourDivisors(nums)
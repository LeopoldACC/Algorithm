class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = dividend*divisor>0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend>divisor:
            l,r = 0,31
            while l<r:
                mid = (l+r+1)//2
                if (1<<mid) * divisor<=dividend:
                    l = mid
                else:
                    r = mid-1
                    
            res+=1<<l
            dividend-=(1<<l)*divisor
        return res if pos else -res
s = Solution()
dividend = 10
divisor = 3
s.divide(dividend,divisor)
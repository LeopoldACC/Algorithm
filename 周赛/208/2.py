class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        sums = 0
        res = 0
        profit = []
        for i in range(len(customers)):
            sums+=customers[i]
            res-=runningCost
            onboard = 4 if sums>=4 else sums
            sums-=onboard
            res+=boardingCost*onboard
            profit.append(res)
        while sums:
            if sums>=4:
                sums-=4
                res+=boardingCost*4-runningCost
            else:
                res+=boardingCost*sums-runningCost
                sums=0
            profit.append(res)
        # print(profit)
        maxi = 0
        for i in range(len(profit)):
            if maxi<profit[i]:
                maxi = profit[i]
                ans = i+1
            
        return ans if maxi>0 else -1
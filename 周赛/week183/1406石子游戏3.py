class Solution0(object):###没做出来
    def stoneGameIII(self, A):
        n = len(A)
        dp = [-float('inf')] * n
        for i in range(n-1,-1,-1):
            dp[i] = max(dp[i], sum(A[i:i+1]) - (dp[i+1] if i+1<n else 0))
            dp[i] = max(dp[i], sum(A[i:i+2]) - (dp[i+2] if i+2<n else 0))
            dp[i] = max(dp[i], sum(A[i:i+3]) - (dp[i+3] if i+3<n else 0))
        if dp[0] == 0:return "Tie"
        if dp[0] > 0:return "Alice"
        if dp[0] < 0:return "Bob"
#用一个数组 dp 来表示“在只剩下第 i 堆到最后一堆石子时，当前玩家最多能拿多少分”。
# 假如算出了这个 dp 数组，那么最终答案就是判断 dp[0] 和（分数总和-dp[0]）之间的大小关系即可  
## dp[0]<su-dp[0] Bob  dp[0]>su-dp[0] Alice(Alice肯定会取到0)
class Solution:###因此有 dp[i]= sum{i,n} - min{dp[i+1],dp[i+2],dp[i+3]}，分别对应取走一堆、两堆、三堆石子的情况。
    def stoneGameIII(self, s):
        su = 0
        dp = [0]*(len(s)+1)+[10000000]*4###从最后取，对手   ###dp[i]不能初始化为s
        for i in range(len(s)-1, -1, -1):
            su += s[i]
            cho = min(dp[i+1],dp[i+2],dp[i+3])
            dp[i] = su - cho
   #    print(dp)
        if dp[0]+dp[0]<su:
            return "Bob"
        elif dp[0]+dp[0]>su:
            return "Alice"
        return "Tie"
class Solution1:
    def stoneGameIII(self, stoneValue):
        dp = stoneValue
        for _ in range(3):
            dp.append(0)

        sumation = 0
        for i in reversed(range(len(dp) - 3)):###不用从最后的3个补0开始走
            sumation += stoneValue[i]
            dp[i] = sumation - min(
                dp[i + 1],
                dp[i + 2],
                dp[i + 3],
            )

        if dp[0] > sumation - dp[0]:
            return 'Alice'
        elif dp[0] < sumation - dp[0]:
            return 'Bob'
        return 'Tie'
s = Solution1()
s.stoneGameIII([1,2,3,7])
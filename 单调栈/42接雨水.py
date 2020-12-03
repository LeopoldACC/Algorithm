class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        l_max = [0]*n
        r_max = [0]*n
        l_max[0] = height[0]
        r_max[n-1] = height[n-1]
        for i in range(1,n):
            l_max[i] = max(l_max[i-1],height[i])
        for i in range(n-2,-1,-1):
            r_max[i] = max(r_max[i+1],height[i])
        res = 0
        for i in range(n):
            res+=min(l_max[i],r_max[i])-height[i]
        return res

# 单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        n = len(height)
        res = 0
        for i in range(n):
            while stk and height[stk[-1]]<=height[i]:
                l = stk.pop()
                if not stk:#左边没有接的住的了
                    break
                res+=(i-stk[-1]-1)*(min(height[stk[-1]],height[i])-height[l])
            stk.append(i)
        return res
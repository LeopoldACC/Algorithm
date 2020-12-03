class Solution:
    def largestRectangleArea(self, heights) -> int:
        stk = []
        heights.append(-1)
        n = len(heights)
        res=0
        # 单增栈 stk pop 出来的cur 右边比cur矮的是i 左边比cur矮的是stk[-1]
        for i in range(n):
            while stk and heights[stk[-1]]>heights[i]:
                cur=stk.pop()
                if stk:
                    res=max(res,(i-stk[-1]-1)*heights[cur])
                else:
                    res=max(res,i*heights[cur])
            stk.append(i)
        return res

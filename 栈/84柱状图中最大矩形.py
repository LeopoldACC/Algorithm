class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        
        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
        
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

# 链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode-/
class Solution1:
    def largestRectangleArea(self, heights) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res
##二刷碰到的问题
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = heights+[0]##第一个heights写成了stack
        res=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:##写成了stack[-1]>heights[i]
                tmp = stack.pop()
                res = max(res,heights[tmp]*(i-stack[-1]-1 if stack else i))
            stack.append(i)
        return res
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res=0,tmp=0;
        stack<int> stk;
        heights.push_back(0);
        for (int i=0;i<heights.size();i++){
            while (!stk.empty() && heights[stk.top()]>heights[i]){
                tmp = stk.top();
                stk.pop();
                res = max(res,heights[tmp]*(stk.empty()?i:i-stk.top()-1));
            }
            stk.push(i);
        }
        return res;
    }
};
# 链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhao-liang-bian-di-yi-ge-xiao-yu-ta-de-zhi-by-powc/
so = Solution1()
h = [2,1,5,6,2,3]
so.largestRectangleArea(h)
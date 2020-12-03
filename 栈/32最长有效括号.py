class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            if s[i]==')':##每次碰到")"必pop，然后pop完stack为空说明
            #右括号比左括号多，那么有效长度起始点就从此时最后append进去的右括号的下标开始
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i-stack[-1])
        return res

# 二刷20201109
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stk = [-1]
        res =0
        for i in range(n):
            if s[i]=='(':
                stk.append(i)
            else:
                l = stk.pop()
                if stk:
                    res = max(res,i-stk[-1])
                else:#啥时候会stk为空 )) 右括号多于左括号导致左括号都没了 那么就需要往stk里放当前')'下标作为之后算长度的起点
                    stk.append(i)
        return res
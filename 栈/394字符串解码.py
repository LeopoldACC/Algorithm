class Solution:
    def decodeString(self, s: str) -> str:
        stack,res,multi = [],'',0
        for c in s:
            if '0'<=c<='9':
                multi = 10*multi+int(c)
            elif c=='[':
                stack.append((res,multi))###append进去的是括号前的res，第一个括号则append进""
                ###漏了定义
                res,multi = "",0###一个新括号里的字符串从空字符串开始  之后碰到字母 res+=c 
            elif c==']':
                ###漏了定义
                pre_res,cur_multi = stack.pop()###出来的是括号前的res
                
                res = pre_res + cur_multi*res
            else:
                res+=c
        return res
class Solution0:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        dic = {')':'(','}':'{',']':'['}
        # for c in s:
        #     if stk:
        #         if stk[-1] == dic[c]:
        #             stk.pop()
        #             continue
        #     stk.append(c)
        for i in range(len(s)):
            if stk and s[i] in dic:#要判断的
                if stk[-1] == dic[s[i]]:
                    stk.pop()
                    continue
            stk.append(s[i])
        return len(stk)==0 
s = "{[]}"
so = Solution()
so.isValid(s)
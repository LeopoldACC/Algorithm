class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if k>=len(num):
            return "0"
        for i in range(len(num)):
            while stack and int(num[i])<int(stack[-1]) and k>0:
                stack.pop()
                k-=1
            stack.append(num[i])
        while k>0:
            stack.pop()
            k-=1
        res = ''.join(stack)
        
        for i in range(len(res)):
            if res[i]=='0':
                continue
            else:
                break
        return res[i:]
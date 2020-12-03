class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        n = len(num)
        remain = n-k
        for ch in num:
            while k and stk and stk[-1]>ch:
                stk.pop()
                k-=1
            stk.append(ch)
        stk = stk[:-k] if k else stk
        if not stk:
            return '0'
        while stk and stk[0]=='0':
            stk = stk[1:]
        return ''.join(stk) if stk else '0'
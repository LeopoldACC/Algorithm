class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_pos = {chr(od):0 for od in range(ord('a'),ord('z')+1)}
        in_stk = {chr(od):False for od in range(ord('a'),ord('z')+1)}
        for i in range(len(s)):
            last_pos[s[i]] = i
        
        for i in range(len(s)):
            while stack and ord(stack[-1])>ord(s[i]) and last_pos[stack[-1]]>=i:###last_pos[stack[-1]] 写成[s[i]]了
                tmp = stack.pop()
                in_stk[tmp] = False
            stack.append(s[i])
            in_stk[s[i]] = True
        
        return ''.join(stack)
s =Solution()
ch = "cbacdcbc"
s.removeDuplicateLetters(ch)
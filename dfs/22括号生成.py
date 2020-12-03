class Solution:
    def generateParenthesis(self, n):
        res = []
        path = []
        l,r = 0,0
        self.dfs(n,l,r,path,res)
        return res
    
    def dfs(self,n,l,r,path,res):
        if len(path)==2*n:
            res.append(''.join(path))
            return 

        if l<n and l>=r:
            path.append('(')
            self.dfs(n,l+1,r,path,res)
            path.pop()###第一次到这是((( 那么pop完之后会继续往下走 ((
        
        ###后面没写出来
        if r<l:##不是<= 而是<
            path.append(')')
            self.dfs(n,l,r+1,path,res)
            path.pop()###第一次到这是((()))
class Solution1:
    def generateParenthesis(self, n: int):
        res = []
        self.dfs('', n, n, res)
        return res
    def dfs(self, temp, left, right, res):
        if left == right == 0:
            res.append(temp)
            return 
        if left > right:
            return 
        if left:
            self.dfs(temp + '(', left - 1, right, res)
        if right:
            self.dfs(temp + ')', left, right - 1, res)

class Solution2:
    def generateParenthesis(self, n: int):
        res = []
        def dfs(path,l,r):
            if len(path)==2*n:
                res.append(path)
            if l<n:
                path+="("
                dfs(path,l+1,r)
                path=path[:-1]
            if r<l:
                path+=")"
                dfs(path,l,r+1)
                path=path[:-1]
        dfs("",0,0)
        return res
s = Solution2()
s.generateParenthesis(1)
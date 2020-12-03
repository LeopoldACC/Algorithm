class Solution1:
    def restoreIpAddresses(self, s: str):
        res = []
        def judge(begin,end):
            ip = 0
            if end-begin+1>1 and s[begin]=='0':
                return -1
            for i in range(begin,end+1):
                ip = ip*10+int(s[i])
            return ip if ip<=255 else -1

        def dfs(path,start):
            if len(path)==4:
                if start==len(s):
                    res.append('.'.join(path))
                return
            for i in range(3):
                if start+i>=len(s):
                    break
                ip = judge(start,start+i)
                if ip!=-1:
                    path.append(str(ip))
                    dfs(path,start+i+1)
                    path.pop()
        dfs([],0)
        return res
class Solution:
    def restoreIpAddresses(self, s: str):
        res=[]
        n = len(s)
        def dfs(path,start):
            if len(path)==4:
                if start==n:
                    res.append('.'.join(path))
                return
            for i in range(start,n):
                seq = s[start:i+1]
                if (seq[0]=='0' and i-start+1>=2) or int(seq)>255:
                    break#用break比continue快了3倍
                path.append(seq)
                dfs(path,i+1)
                path.pop()
        dfs([],0)
        return res
s = Solution()
string = "25525511135"
res = s.restoreIpAddresses(string)
print(res)
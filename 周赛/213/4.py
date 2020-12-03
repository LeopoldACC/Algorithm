class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        C = [[1] * 31 for _ in range(31)]
        for i in range(31):
            for j in range(i+1):
                if j==0 or i==j:
                    C[i][j] = 1
                else:
                    C[i][j] = C[i-1][j-1]+C[i-1][j]

        # 总共的长度==m+n 排列的种数 = C{n}{m+n}
        m,n = destination[0],destination[1]
        res = ''
        for i in range(m+n):
            if n>0:#优先"H"
                o = C[m+n-1][n-1]#当前位置选H 剩余m+n-1位中有n-1位H 总数=C[m+n-1][n-1]
                if k>o:#如果比这个大 说明k在的区间需要当前位置选V
                    res+='V'
                    m-=1
                    k-=o#剩余字典序
                else:#否则 说明k在的区间需要当前位置选H
                    res+='H'
                    n-=1
            else:#如果没有"H"了 那就只能选"V"了
                res+='V'
                m-=1
        return res
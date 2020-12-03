class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = []
        d = 0
        for c in seq:
            if c=='(':
                res.append(d%2)
                d+=1
            else:
                d-=1
                res.append(d%2)
        return res
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans=[0]
        for i in range(1,len(seq)):
            ans.append(1-ans[i-1]) if seq[i]==seq[i-1] else ans.append(ans[i-1])
        return ans
###只要连续两个((或))分在不同组就行了
#链接：https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/solution/pythonyou-xiao-gua-hao-de-qian-tao-shen-du-by-jutr/

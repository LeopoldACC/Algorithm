# 单调栈
## Leetcode 84柱状图中的最大矩形
1. 找到每个柱形条左边和右边最近的比自己低的矩形条，然后用宽度乘上当前柱形条的高度作为备选答案。
2. 此类问题的经典做法是单调栈，维护一个单调递增的栈，如果当前柱形条`i` 的高度比栈顶要低，则栈顶元素 `cur` 出栈。出栈后，`cur` 右边第一个比它低的柱形条就是 `i`，左边第一个比它低的柱形条是当前栈中的 `top`。不断出栈直到栈为空或者柱形条 `i` 不再比 `top` 低。
3. 每个`i`都入栈
4. 最后append一个高度为-1的柱形条让所有柱子出栈

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        heights.append(-1)
        n = len(heights)
        res=0
        for i in range(n):
            while stk and heights[stk[-1]]>heights[i]:
                cur=stk.pop()
                #如果栈中没有元素 说明cur左边没有比cur更小的了,则最左可以到0(最大宽度=i-0=0) 
                if stk:
                #所以当前最大矩形面积=
                    res=max(res,(i-stk[-1]-1)*heights[cur])
                #否则 当前高度的宽度=i(右边比cur小的有右边界界)-stk[-1](左边比cur小的左边界)-1
                else:
                    res=max(res,i*heights[cur])
            stk.append(i)
        return res
```
## Leetcode 85最大矩形
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
---------  比如到第三行 heights = [3,1,3,2,2]
1 0 0 1 0
```
则问题转化为84题
```
|   |
|   | | |
| | | | |
```

逐行递归 对每一行

得到每行中每一列的高度`heights[i][j]`

1. 如果`mat[i][j]==0`则对当前行"柱子"高度`heights[j]=0` 

2. 否则`heights[i][j]=heights[i-1][j]+1`

为了省空间 因为前一行`heights[j]`用完后对于下一行就是`heights[i-1][j]+1`,则`heights[i-1][j]+1`完全可以用一行来更新:

即`heights[j] = heights[j]+1`

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])
        height = [0]*(n+1)
        res = 0
        for i in range(m):
            stk = []
            for j in range(n+1):
                #height[n]=0是哨兵 用来把所有柱子弄出来的 所以不用设值也不能设值
                if j<n:
                    if matrix[i][j]=='1':
                        height[j]+=1
                    else:
                        height[j]=0
                while stk and height[j]<height[stk[-1]]:
                    cur = stk.pop()
                    if stk:
                        res = max(res,(j-stk[-1]-1)*height[cur])
                    else:
                        res = max(res,j*height[cur])
                stk.append(j)
        return res
```
# 最小数字、最小字典序问题
# Leetcode402 移掉K位数字
思考为什么要用单调性?
因为单增的情况
num = 1234567  k = 2 时就删最后两位就行

如果出现递减
num = 1234**52**6  k = 2 
对`526` `5>2`则用更低位的2替换更高位的5 num肯定减少 
同理对42也是

所以用单调增栈维护当前前i位数构成的数如果出现**递减**,则删除栈顶
```python
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
```

# Leetcode1081不同字符的最小子序列/316去除重复字母
与上面题目不同，这道题没有一个全局的删除次数 k。而是对于每一个在字符串 s 中出现的字母 c 都有一个 k 值。这个 k 是 c 出现次数 - 1。

沿用上面的知识的话，我们首先要做的就是计算每一个字符的 k，可以用一个字典来描述这种关系，其中 key 为 字符 c，value 为其出现的次数。
```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stk = []
        k_cnt = collections.Counter(s)
        n = len(s)
        for c in s:
            if c not in stk:#只需要出现一次 如果加进去后 后面没有比c更小的则会多一个重复的c
                while stk and c<stk[-1] and k_cnt[stk[-1]]>0:#k_cnt[stk[-1]]>0代表后面还有skt[-1]可以加进来 所以就算pop完了也没关系
                    stk.pop()
                stk.append(c)
            k_cnt[c]-=1
        return ''.join(stk)
```

# Leetcode321
我们将从 num1 中挑选的 k1 个数组成的数组称之为 A，将从 num2 中挑选的 k2 个数组成的数组称之为 B，

**在很多编程语言中：如果 A 和 B 是两个数组，当前仅当 A 的首个元素字典序大于 B 的首个元素，A > B 返回 true，否则返回 false。**

```
example
A = [1,2]
B = [2]
A < B # True

A = [1,2]
B = [1,2,3]
A < B # False
```
取法通过单调递减栈维护
```
example
[9 1 2 5 8 3] k =3
[9 8 3]
```

```python
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(nums,k):
            stk = []
            drop = len(nums)-k#从A中取k个 则最多能pop len(A)-k个
            for num in nums:
                while drop and stk and stk[-1]<num:#还能pop drop个 stk[-1]<num维护单减 
                    stk.pop()
                    drop-=1
                stk.append(num)
            return stk[:k]
        def merge(A,B):
            res = []
            while A or B:
                bigger = A if A>B else B
                res.append(bigger[0])
                bigger.pop(0)
            return res
        
        return max(merge(pick_max(nums1,i),pick_max(nums2,k-i)) for i in range(k+1) if i<=len(nums1) and k-i<=len(nums2))
```
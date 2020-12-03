class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # 状态压缩,枚举每一种状态下,是否满足点的出入度相同,记录最大值即可
        ans = 0
        m = len(requests)
        bit = 1 << m
        for i in range(bit):
            temp = 0
            degree = [0] * n
            for j in range(m):
                if (i >> j) & 1:
                    temp += 1
                    degree[requests[j][0]] += 1
                    degree[requests[j][1]] -= 1
            tag = 1
            # 判断当前选择边是否满足
            for k in range(n):
                if degree[k] != 0:
                    tag = 0
                    break
            if tag:
               ans = max(ans,temp)
        return ans
# https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests/solution/py3-zhuang-tai-ya-suo-by-wzhaooooo-2/

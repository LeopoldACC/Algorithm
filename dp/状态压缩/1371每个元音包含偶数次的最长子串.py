#https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/solution/zhuang-tai-ya-suo-ji-lu-yuan-yin-zi-mu-chu-xian-qi/
# 为什么想到前缀和  因为假设[l,r]符合元音偶数要求，以0为偶数状态，1为奇数状态的话
# 那么[0,r]和[0,l-1]就是一个状态
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        whole_state = [float('inf')]*32
        whole_state[0]=0
        yy = 'aeiou'
        res = 0###不能初始化为len(s)
        state = 0
        for i in range(1,len(s)+1):###为什么要从1开始，因为i记录的是长度而不仅仅是减
            for j in range(5):
                if s[i-1]==yy[j]:###从1开始，所以对比的时候要-1
                    state^=1<<j
            whole_state[state] = min(whole_state[state],i)###为什么要从1开始，因为i记录的是长度而不仅仅是减
            res = max(i-whole_state[state],res)
        return res    
# O(n) 最长连续序列
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)
        
        for num in num_set:
            # 能作为起点就开始往上逐步加1
            if num - 1 not in num_set:
                # 初始化长度=1
                current_num = num
                current_streak = 1
                # 只要能找到连续大1的就继续+1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

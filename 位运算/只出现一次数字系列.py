# 136. 只出现一次的数字1
class Solution136:
    def singleNumber(self, nums):
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number
# 137. 只出现一次的数字2 
class Solution137:
    def singleNumber(self, nums):
        res = 0
        for i in range(32):
            cnt = 0  # 记录当前 bit 有多少个1
            bit = 1 << i  # 记录当前要操作的 bit
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0:
                # 不等于0说明唯一出现的数字在这个 bit 上是1
                res |= bit

        return res - 2 ** 32 if res > 2 ** 31 - 1 else res
# 645. 错误的集合
class Solution645:
    def singleNumbers(self, nums):
        ret = 0  # 所有数字异或的结果
        a = 0
        b = 0
        for n in nums:
            ret ^= n
        # 找到第一位不是0的
        h = 1
        while(ret & h == 0):
            h <<= 1
        for n in nums:
            # 根据该位是否为0将其分为两组
            if (h & n == 0):
                a ^= n
            else:
                b ^= n

        return [a, b]

    def findErrorNums(self, nums):
        nums = [0] + nums
        idx = []
        for i in range(len(nums)):
            idx.append(i)
        a, b = self.singleNumbers(nums + idx)
        for num in nums:
            if a == num:
                return [a, b]
        return [b, a]

#260 只出现一次的数字3
class Solution260:
    def singleNumbers(self, nums):
        ret = 0  # 所有数字异或的结果
        a = 0
        b = 0
        for n in nums:
            ret ^= n
        # 找到第一位不是0的
        h = 1
        while(ret & h == 0):
            h <<= 1###<<=

        for n in nums:
            # 根据该位是否为0将其分为两组
            if (h & n == 0):
                a ^= n###这一位上可能有其他重复的数也为1 不能a=n
            else:
                b ^= n

        return [a, b]
# s = Solution137()
# nums = [0,1,0,1,0,1,99]
# s.singleNumber(nums)

s2 = Solution260()
nums2 = [3,2,1,3]
s2.singleNumbers(nums2)
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/zhi-chu-xian-yi-ci-de-shu-xi-lie-wei-yun-suan-by-a/

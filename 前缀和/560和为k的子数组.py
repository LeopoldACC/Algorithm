class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = {0:1}#边界处理 考虑前缀和为0的情况
        sums,res=0,0
        for num in nums:## k=2 nums [2 1 -1 -2] sums [2 3 2 0]  res[1 0 2 2]
            sums+=num
            res+=prefix_sum.get(sums-k,0)###前面出现过的位置的前缀和与当前index前缀和刚好差k的个数
            prefix_sum[sums] = prefix_sum.get(sums,0)+1###num有正有负  所以存在前后前缀和相同的情况  2 -1 1 
        return res
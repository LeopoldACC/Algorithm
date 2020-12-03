class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        n = len(nums)
        s = [0]+nums[:]
        assist = [0]*(n+1)
        for i in range(1,n+1):
            s[i]+=s[i-1]
        # 为什么要归并排序-- s[i]-s[j] i>j 则分治时刚好维护了两边j<i
        def merge(s,assist,l,r,low,up):
            if l>=r:return 0
            cnt = 0
            m = l+(r-l)//2
            # 递归到下面
            cnt+=merge(s,assist,l,m,low,up)
            cnt+=merge(s,assist,m+1,r,low,up)
            # 对当前区间 分为左区间和右区间 
            left = l
            upper = m+1
            lower = m+1
            # 对左区间的每一个left 
            # 对右区间找第一个s[lower]-s[left]>=low
            # 对右区间找第一个s[upper]-s[left]>up 
            while left<=m:
                while lower<=r and s[lower]-s[left]<low:lower+=1
                while upper<=r and s[upper]-s[left]<=up:upper+=1
                cnt+=upper-lower
                left+=1
            # 归并排序
            left = l
            right = m+1
            pos = l
            while left<=m or right<=r:
                if left>m:
                    assist[pos] = s[right]
                    right+=1
                if right>r and left<=m:
                    assist[pos] = s[left]
                    left+=1
                if left<=m and right<=r:
                    if s[left]<=s[right]:
                        assist[pos] = s[left]
                        left+=1
                    else:
                        assist[pos] = s[right]
                        right+=1
                pos+=1
            for i in range(l,r+1):
                s[i] = assist[i]
            # 回溯到更大的区间
            return cnt
        return merge(s,assist,0,n,lower,upper)
s = Solution()
nums = [2147483647,-2147483648,-1,0]
lower = -1
upper = 0
s.countRangeSum(nums,lower,upper)

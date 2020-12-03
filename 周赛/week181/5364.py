class Solution:
    def createTargetArray(self, nums, index):
        
        n=len(nums)
        res = [0]*n
        
        for i in range(1,len(index)):
            for j in range(0,i):
                if index[j]>=index[i]:
                    index[j] +=1
        for i in range(n):
            res[index[i]] = nums[i]
        return res
s =Solution()
nums = [4,2,4,3,2]
index = [0,0,1,3,1]
print(s.createTargetArray(nums,index))
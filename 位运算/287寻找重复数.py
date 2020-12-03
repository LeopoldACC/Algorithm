class Solution:
    def findDuplicate(self, nums):
        n,res,bit_max= len(nums),0,31
        while n-1>>bit_max==0:
            bit_max-=1
        for bit in range(bit_max+1):
            x,y = 0,0
            for i in range(n):
                if nums[i] & 1<<bit:
                    x+=1
                print("i:%d,1<<bit:%d,i&1<<bit:%d"%(i,1<<bit,i&1<<bit))
                if i>=1 and i&1<<bit:
                    y+=1
            if x>y:
                res |= 1<<bit
        return res
s =Solution()
nums = [1,3,4,2,2]
s.findDuplicate(nums)
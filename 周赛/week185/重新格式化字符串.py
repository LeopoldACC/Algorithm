class Solution:
    def reformat(self, s: str) -> str:
        nums_e,nums='',''
        res = ''
        for ch in s:
            if ord('a')<=ord(ch)<=ord('z'):
                nums_e+=ch
            else:
                nums+=ch
        if len(nums_e)>len(nums)+1 or len(nums_e)<len(nums)-1:
            return ''
        
        l,r=0,0
        
        if len(nums_e)>len(nums):
            res+=nums_e[l]
            l+=1
            while r<len(nums):
                res+=nums[r]
                r+=1
                res+=nums_e[l]
                l+=1
                
        if len(nums_e)<len(nums):
            res+=nums[r]
            r+=1
            while l<len(nums_e):
                res+=nums_e[l]
                l+=1
                res+=nums[r]
                r+=1
        else:
            while l<len(nums_e):
                res+=nums_e[l]
                l+=1
                res+=nums[r]
                r+=1
        return res
s = Solution()
s.reformat("ab123")
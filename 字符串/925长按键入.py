class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name and typed or name and not typed or len(name)>len(typed):
            return False
        l,r = 0,0
        while l<len(name) and r<len(typed):
            if name[l]==typed[r]:
                l+=1
                r+=1
            elif r>0 and typed[r]==typed[r-1]:
                r+=1
            else:
                return False
        if l==len(name):
            for i in range(r,len(typed)):
                if typed[i]!=name[l-1]:
                    return False    
            return True
        
s = Solution()

s.isLongPressedName(
    "alex",
    "aaleex"
)
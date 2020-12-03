class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count =0 
        while m!=n:#找公共前缀
            m >>=1
            n >>=1
            count+=1
        return m << count


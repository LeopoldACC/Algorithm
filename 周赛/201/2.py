class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        string = "0"
        while n>0:
            n-=1
            reverse = ''
            for i in range(len(string)):
                reverse+='1' if string[i]=='0' else '0'
            string = string+"1"+reverse[::-1]
            print(string)
        return string[k]
s = Solution()
s.findKthBit(3,1)
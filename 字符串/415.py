class Solution:
    def addStrings(self, num1: str, num2: str) -> str:        
        num1 = '0'+num1
        num2 = '0'+num2
        m,n = len(num2),len(num1)
        if m>n:#保证n更大
            num1,num2 = num2,num1
            m,n = n,m
        rem = 0
        
        for i in range(n-1,n-m-1,-1):
            sums = int(num1[i])+int(num2[m-1-(n-1-i)])+rem
            num1= num1[:i] + str(sums%10) + num1[i+1:] 
            rem = 1 if sums>=10 else 0
        if rem>0:
            for i in range(n-m-1,-1,-1):
                sums = int(num1[i])+rem
                num1 = num1[:i] + str(sums%10) + num1[i+1:]
                rem = 1 if sums>=10 else 0
        if num1[0] == '0':
            num1 = num1[1:]
        return num1
s= Solution()
ls = [["9","99"],["6994","36"],["71","168899993"]]
for str1,str2 in ls:
    s.addStrings(str1,str2)
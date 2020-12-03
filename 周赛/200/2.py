class Solution:
    def getWinner(self, arr, k: int) -> int:
        n = len(arr)
        if k>n:
            return max(arr)
        i,j = 0,1#i存大的数
        cnt = {x:0 for x in arr}
        m = k
        while True:
            if arr[i]>arr[j]:
                arr.append(arr[j])
                j=j+1
            else:
                cnt[arr[i]]=0
                arr.append(arr[i])
                i = j
                j=j+1
            
            cnt[arr[i]]+=1
            if cnt[arr[i]]==m:
                return arr[i]
            
        
            
s = Solution()
arr = [2,1,3,5,4,6,7]
k = 2
s.getWinner(arr,k)
###归并排序
# 分治
# 合并
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.res = 0
        self.mergeSort(nums,0,len(nums)-1)
        return self.res
    
    def mergeSort(self,nums,start,end):#分治
        if start>=end:
            return 
        mid = (start+end)//2
        self.mergeSort(nums,start,mid)
        self.mergeSort(nums,mid+1,end)
        self.merge(nums,start,mid,end)

    def merge(self,nums,start,mid,end):
        i,j,temp = start,mid+1,[]
        while i<=mid and j<=end:
            if nums[i]<=nums[j]:
                temp.append(nums[i])
                i+=1
            else:
                temp.append(nums[j])
                j+=1
                self.res+=mid-i+1
        while i<=mid:
            temp.append(nums[i])
            i+=1
        while j<=end:
            temp.append(nums[j])
            j+=1
        nums[start:start+len(temp)] = temp


class MountainArray:
    def __init__(self,mountain_arr):
        self.mountain_arr = mountain_arr
    def get(self, index):
        return self.mountain_arr[index]
    def length(self):
        return len(self.mountain_arr)
class Solution:###14.4%
    def findInMountainArray(self, target, mountain_arr):
        l,r=0,mountain_arr.length()-1
        while l+1<r:
            mid = (l+r)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                l = mid
            else:
                r = mid
        if mountain_arr.get(l)>mountain_arr.get(r):
            peak = l
        else:
            peak = r
        in_left = self.binary_search_l(mountain_arr,0,peak,target)
        if in_left!=-1:
            return in_left
        in_right = self.binary_search_r(mountain_arr,peak,mountain_arr.length()-1,target)
        return in_right

    def binary_search_l(self,mountain_arr,start,end,target):
        l,r=start,end    
        while l+1<r:
            mid = (l+r)//2
            if mountain_arr.get(mid)<target:
                l=mid
            else:
                r=mid
        
        if mountain_arr.get(l)==target:
            return l
        if mountain_arr.get(r)==target:
            return r
        return -1
    def binary_search_r(self,mountain_arr,start,end,target):
        l,r=start,end    
        while l+1<r:
            mid = (l+r)//2
            if mountain_arr.get(mid)<target:
                r=mid
            else:
                l=mid
        
        if mountain_arr.get(l)==target:
            return l
        if mountain_arr.get(r)==target:
            return r
        return -1
class Solution1:###80%
    def findInMountainArray(self, target, mountain_arr):
        l,r=0,mountain_arr.length()-1
        while l+1<r:
            mid = (l+r)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                l = mid
            else:
                r = mid
        if mountain_arr.get(l)>mountain_arr.get(r):
            peak = l
        else:
            peak = r
        in_left = self.binary_search(mountain_arr,0,peak,target)
        if in_left!=-1:
            return in_left
        in_right = self.binary_search(mountain_arr,peak,mountain_arr.length()-1,target,lambda x:-x)
        return in_right

    def binary_search(self,mountain_arr,start,end,target,key = lambda x:x):
        target = key(target)
        l,r=start,end    
        while l+1<r:
            mid = (l+r)//2
            if key(mountain_arr.get(mid))<target:
                l=mid
            else:
                r=mid
        
        if key(mountain_arr.get(l))==target:
            return l
        if key(mountain_arr.get(r))==target:
            return r
        return -1
m = MountainArray([0,5,3,1])
t = 1
s = Solution1()
s.findInMountainArray(t,m)

class Solution_False:
    def minArray(self, nums):
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[mid+1] and nums[mid]<=nums[-1]:
                r = mid#在右边
            elif nums[mid]<=nums[mid+1] and nums[mid]>nums[-1]:
                l = mid+1#在左边
            else:
                return nums[mid+1]
        return nums[l]

class Solution:
    def minArray(self, nums):
        l,r = 0,len(nums)-1
        if nums[0]<nums[-1]:
            return nums[0]
        while l<r:
            mid = (l+r)//2
            if nums[mid]<=nums[mid+1]:#比的应该是右边而不是最后一个，然后才能在第三种情况去-1
                if nums[mid]<nums[r]:
                    r = mid#在右边
                elif nums[mid]>nums[r]:
                    l = mid+1#在左边
                else:#mid==nums[r]==nums[l] 这个时候只需要把右边的一直往左移直到nums[mid]>nums[r]
                    r-=1
            else:
                return nums[mid+1]
            
        return nums[l]
nums = [
    [1,3,5],
[3,4,5,1,2],
[2,2,2,0,1],
[3,3,3,3,3,3,3,3,1,3]
]
s = Solution()
for i in range(len(nums)):
    s.minArray(nums[i])

class Solution {
public:
    int minArray(vector<int>& nums) {
        int l=0,r=nums.size()-1;
        while(l<r)
        {
            int mid = (l+r)/2;
            if (nums[mid]<=nums[mid+1])
            {
                if(nums[mid]>nums[r]) l=mid+1;
                else if(nums[mid]<nums[r]) r= mid;
                else r--;
            }
            else return nums[mid+1];
        }
        return nums[l];
    }
};
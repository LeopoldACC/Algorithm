class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # node = index of nums
        # node.next = nums[node]
        # node.next.next = nums[nums[node]]
        slow = nums[0]         #先走一步
        fast = nums[nums[0]] 
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]] # 曾经犯的一个错误，以后这里会在值相同的那个点相遇
        root = 0                    # 但是它们可以在任何一个node相遇，这里就是任何一个index的坐标    
        while root != slow:
            root = nums[root]
            slow = nums[slow]
        return slow             # 回到循环结束前的上一步
                                # nums[prefixRoot] == nums[prefixSlow]
                                # so slow is the value in the array which at least have two slot

# 链接：https://leetcode-cn.com/problems/find-the-duplicate-number/solution/miao-dong-kuai-man-zhi-zhen-by-wo-you-dian-ben/

s =Solution()
nums = [5,5,5,2,5,5]
# nums = [2,2,2,2,2]
res = s.findDuplicate(nums)
print(res)
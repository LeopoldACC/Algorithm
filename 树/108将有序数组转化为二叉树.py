# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        dic = set()
        def partition(l,r):
            if l>r:
                return None
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = partition(l,mid-1)#为什么-1 因为mid的话会第二次遍历到mid，然后出递归出口就设成了l>=r
            root.right = partition(mid+1,r)
            return root
        return partition(0,len(nums)-1)
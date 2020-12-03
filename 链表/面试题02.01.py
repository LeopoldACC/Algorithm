# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self,nums):
        self.nums = nums
        self.input = self.createLinkedList(nums)
        self.res = self.removeDuplicateNodes()
        self.output = self.printLinkedList()

    def removeDuplicateNodes(self):
        dic = set()
        dummy = ListNode(0)
        head = self.input
        dummy.next = head
        while head and head.next:
            dic.add(head.val)###字典不能直接存链表节点 因为有相同val的链表节点内存地址不同
            while head.next and head.next.val in dic:###判断的时候同理
                head.next = head.next.next
            head = head.next
        return dummy.next

    def createLinkedList(self,nums):
        if not nums:
            return None
        dummy = ListNode(0)
        head = ListNode(nums[0])
        dummy.next = head
        for i in range(1,len(nums)):
            head.next = ListNode(nums[i])
            head = head.next
        return dummy.next

    def printLinkedList(self):
        res = []
        head = self.res
        while head:
            res.append(head.val)
            head= head.next
        print(res)



nums = [1, 2, 3, 3, 2, 1]
so = Solution(nums)
so.removeDuplicateNodes()
so.printLinkedList()
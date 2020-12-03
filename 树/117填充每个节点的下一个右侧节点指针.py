#空间O(n)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = collections.deque([])
        q.append(root)
        while q:
            pre = None
            for i in range(len(q)):
                t = q.popleft()
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
                if pre:
                    pre.next = t
                pre = t
        return root

#空间O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        head = root
        
        while head:
            # 链表头节点 dummy 尾节点 tail
            dummy = Node(0)
            tail = dummy
            while head:
                # 将当前节点的左右儿子加入链表
                if head.left:
                    tail.next = head.left
                    tail = tail.next
                if head.right:
                    tail.next = head.right
                    tail = tail.next
                # 当前节点右移
                head = head.next
            # 此时第i层的所有i+1层儿子都加入了链表(同时第i+1层头节点=dummy.next)
            head = dummy.next
        return root


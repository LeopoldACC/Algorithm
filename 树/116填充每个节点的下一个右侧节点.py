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
                if i==len(q)-1:
                    t.next =None
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
                if pre:
                    pre.next = t
                pre = t
        return root
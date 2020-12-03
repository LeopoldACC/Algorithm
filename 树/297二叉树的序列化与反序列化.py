# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        if not root:
            return []
        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append("null")
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1].split(',')
        if not data: return ""
        i = 0
        root = TreeNode(int(data[i]))
        q = collections.deque([root])
        while q:
            if i>=len(data)-1:
                return root
            node = q.popleft()
            i+=1
            if data[i] !="null":
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i+=1
            if data[i] !="null":
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
        return root
S = Codec()
a = S.deserialize("[1,2,3,null,null,4,5]")
print(S.serialize(a))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

###先从树序列化再反序列化
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        if not root:
            return []
        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append('null')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')###data[1:-1] 不用[1:-1] 因为我们是先从树生成的 ','.join(res) 所以没有开头的[ 和结尾的]
        if not data: return ""
        i = 0
        root = TreeNode(int(data[i]))
        q = collections.deque([root])
        while q:
            if i>=len(data)-1:
                return root
            node = q.popleft()
            i+=1
            if data[i] !='null':
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i+=1
            if data[i] !='null':
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
        return root

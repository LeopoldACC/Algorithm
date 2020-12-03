class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def recoverFromPreorder(self, S: str):
        path, pos = list(), 0
        while pos < len(S):
            level = 0
            while S[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < len(S) and S[pos].isdigit():##pos < len(S) 如果不判断python报错 C++则一直+
                value = value * 10 + (ord(S[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)
            if level == len(path):
                if path:#为什么要在里面做判断，因为如果path为空，len(path)==0==level此时path[-1]是没有的，那么它会去else里调用path[-1]
                    path[-1].left = node
            else:
                path = path[:level]#这里相当于pop至path长度等于level
                path[-1].right = node
            path.append(node)###忘了append当前树节点了
        return path[0]

s = Solution()
string = "1-2--3--4-5--6--7"
s.recoverFromPreorder(string)
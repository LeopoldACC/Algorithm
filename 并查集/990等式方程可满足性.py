class Solution:

    class UnionFind:
        def __init__(self):
            self.parent = list(range(26))
        
        def find(self, index):
            if index == self.parent[index]:#如果自己就是自己的父节点 就返回自己
                return index
            self.parent[index] = self.find(self.parent[index])#如果不是，从自己的父结点开始迭代  
            return self.parent[index]
        
        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)#合并->把index1的父亲节点self.parent[self.find(index1)]


    def equationsPossible(self, equations):
        uf = Solution.UnionFind()
        for st in equations:
            if st[1] == "=":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                uf.union(index1, index2)
        for st in equations:
            if st[1] == "!":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):#这个时候是看!=之前有没有==，如果有那么uf.find(index1)==uf.find(index2)
                    return False
        return True

s = Solution()
ls = ["a==z","a==b","b==c","c==d","b==y","c==x","d==w","g==h","h==i","i==j","a==g","j!=y"]
s.equationsPossible(ls)
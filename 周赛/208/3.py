class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.son = {kingName:[]}
        self.dead = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.son[parentName] = self.son.get(parentName,[])
        self.son[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self):
        def dfs(name):
            path = [name]
            if name not in self.son:
                return path
            for ne in self.son[name]:
                path+=dfs(ne)
            return path
        res =[]
        for x in dfs(self.king):
            if x in self.dead:continue
            res.append(x) 
        return res
t= ThroneInheritance("king");# // 继承顺序：king
t.birth("king", "andy"); #// 继承顺序：king > andy
t.birth("king", "bob");# // 继承顺序：king > andy > bob
t.birth("king", "catherine"); #// 继承顺序：king > andy > bob > catherine
t.birth("andy", "matthew"); #// 继承顺序：king > andy > matthew > bob > catherine
t.birth("bob", "alex"); #// 继承顺序：king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); #// 继承顺序：king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); #// 返回 ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); #// 继承顺序：king > andy > matthew > bob（已经去世）> alex > asha > catherine
t.getInheritanceOrder();# // 返回 ["king", "andy", "matthew", "alex", "asha", "catherine"]
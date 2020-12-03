class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import random
        self.nums = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        if val in self.idx and len(self.idx[val])>=1:
            self.idx[val].add(len(self.nums)-1)
            return False
        else:
            self.idx[val] = set()
            self.idx[val].add(len(self.nums)-1)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.idx:
            return False
        i = self.idx[val].pop()#随机弹出一个
        # self.idx[val].pop()
        self.nums[i] = self.nums[-1]
        if i!=len(self.nums)-1:#当4 2 4 pop出来的i==2时 相当于已经remove了len(self.nums)-1了 这时如果再次remove(len(self.nums)-1)就会报错了
            self.idx[self.nums[i]].remove(len(self.nums)-1) 
        if i<len(self.nums)-1:#新的值 多了一个下标是i的位置
            self.idx[self.nums[i]].add(i)
        if len(self.idx[val])==0:
            del self.idx[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.nums[int(random.random()*len(self.nums))]


op = ["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","remove"]
val = [[],[4],[3],[4],[2],[4],[4],[3],[4],[4]]
# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
for i in range(1,len(op)):
    if op[i]!="getRandom":
        eval("obj."+op[i]+"("+str(val[i][0])+")")
    


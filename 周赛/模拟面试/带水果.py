class Solution:
    def totalFruit(self, tree) -> int:
        
        if not tree:
            return 0
        if len(tree) <3:
            return len(tree)
        in_ls = set([tree[0],tree[1]])
        res=2
        l,r=0,2
        while r<len(tree):
            if tree[r] in in_ls:
                res = max(res,r-l+1)
                r+=1
                if r>=len(tree):
                    return max(res,r-l)
            else:
                in_ls.add(tree[r])
                if len(in_ls)>2:
                    for x in in_ls:
                        if x!=tree[r] and x!=tree[r-1]:
                            x_to_remove = x
                            break
                    in_ls.remove(x_to_remove)
                    l = r-1
                    while tree[l] in in_ls:
                        l-=1
                    l+=1
                    res = max(res,r-l+1)
        return res
s = Solution()
q = [0,1,2,2]
q = [1,2,1]
q = [3,3,3,1,2,1,1,2,3,3,4]
res = s.totalFruit(q)
print(res)
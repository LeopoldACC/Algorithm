class Solution0:###自己的
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        dic={'a':a,'b':b,'c':c}
        maxi = max(dic,key=dic.get)
        re = sum(dic.values())-max(dic.values())
        
        res =''
        if (re+1)*2<=dic[maxi]:
            re_dic = dic
            del(re_dic[maxi])
            for i in re_dic.keys():
                if re_dic[i]!=0:
                    res+=maxi
                    res+=maxi
                    res+=i
                else:
                    continue
        return res
##思路：
# 任何时刻都选择当前存量最多的字符
# 例外：当前两个字符相同时，将该字符排除在候选之外
# 初始存量优化：如何单一字符最大数量必须小于另外（两个字符+1）*2，如‘aabaabaacaa',b与c插入到a序列中，a的数量最多为8。

class Solution1:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = {'a':min(a,2*(b+c+1)),'b':min(b,2*(a+c+1)),'c':min(c,2*(b+a+1))}
        n = sum(d.values())
        res = []
        for i in range(n):
            cand = set(['a','b','c'])
            if len(res)>1 and res[-1]==res[-2]:
                cand.remove(res[-1])
            tmp = max(cand,key=lambda x:d[x])
            res.append(tmp)
            d[tmp] -= 1
        return ''.join(res)

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count ={'a':min(a,(b+c+1)*2),'b':min(b,(a+c+1)*2),'c':min(c,(a+b+1)*2)}
        n = sum(count.values())###总共可取数
        res = ''
        for _ in range(n):
            candidate = set(['a','b','c'])###list传进set自动变为 set
            if len(res)>1 and res[-1]==res[-2]:
                candidate.remove(res[-1])
            tmp = max(candidate,key = lambda x:count[x])###lambda实现字典最大值对应键值
            res+=tmp
            count[tmp]-=1
        return res
###https://blog.csdn.net/sinat_38068807/article/details/86021686
                
          
s = Solution()
a ,b, c =1,1,7
s.longestDiverseString(a,b,c)
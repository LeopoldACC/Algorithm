class Solution:
    def displayTable(self, orders):
        dic = {}
        cai = []
        res = []
        for order in orders:
            if order[2] not in cai:
                cai.append(order[2])
            dic[order[1]] = dic.get(order[1],{})
            dic[order[1]][order[2]] = dic[order[1]].get(order[2],0)+1
        cai.sort()
        cai_i = {cai[i]:i for i in range(len(cai))}
        keys = list(dic.keys())
        keys.sort(key = lambda x:int(x))
        table = {keys[i]:i for i in range(len(keys))}
        res =[["0"] * (len(cai)+1) for _ in range(len(table)+1)]
        res[0][0]="Table"
        for i in range(len(cai)):
            res[0][i+1] = cai[i]
        for j in range(len(table)):
            res[j+1][0] = keys[j]
        for t in keys:
            for t_cai in dic[t]:
                res[table[t]+1][cai_i[t_cai]+1] = str(dic[t][t_cai])
        return res

s = Solution()
orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
orders =[["ZmdDG","16","mrbRX"],["pt","1","mrbRX"],["Hl","5","qrzo"],["jRyk","12","mrbRX"],[" sPzn","8","ijzu"],["KHxC","11","JyY"],["Qqox","2","iA"],["aYWSw","11","ZHmJR"],["onh","5","tGvXE"]]
s.displayTable(orders)

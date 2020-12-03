class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        dic = {i:set(favoriteCompanies[i]) for i in range(len(favoriteCompanies))}
        issubset = [False]*len(favoriteCompanies)
        res = []
        for i in dic:
            if issubset[i]:
                continue
            for j in dic:
                if i==j:
                    continue
                if dic[i].issubset(dic[j]):
                    issubset[i]=True
                if dic[j].issubset(dic[i]):
                    issubset[j]=True
            if not issubset[i]:
                res.append(i)
        #不用sort也行
        return res
s = Solution()
favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
#[["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
a = s.peopleIndexes(favoriteCompanies)
print(a)
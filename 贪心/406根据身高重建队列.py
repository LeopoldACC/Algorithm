class Solution:
    def reconstructQueue(self, people):
        people.sort(key = lambda x:(-x[0],x[1]))
        res=[]

        for i in people:
            res[i[1]:i[1]] = [i]
        return res
import heapq
class Solution:
    def arrangeWords(self, text: str) -> str:
        ls = text.split()
        order = {}
        orderls = []
        heapq.heapify(orderls)
        res = ''
        for ch in ls:
            l = len(ch)
            if l not in order:
                order[l] = [ch]
                heapq.heappush(orderls,l)
            else:
                order[l].append(ch)
        while orderls:
            length = heapq.heappop(orderls)
            for cha in order[length]:
                res+=cha
                res+=' '
        res.capitalize()
        return res
s = Solution()
text = "Leetcode is cool"
s.arrangeWords(text)
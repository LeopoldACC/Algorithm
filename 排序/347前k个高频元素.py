class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {x:0 for x in nums}
        for num in nums:
            cnt[num] += 1
        s = [[cnt[num],num] for num in cnt]
        s.sort()
        res = []
        # print(s)
        for i in range(len(s)-1,len(s)-k-1,-1):
            res.append(s[i][1])
        return res
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cnt = {x:0 for x in nums}
        for num in nums:
            cnt[num] += 1
        count2num = [False]*(n+1)
        for num in cnt:
            if not count2num[cnt[num]]:
                count2num[cnt[num]] = []
            count2num[cnt[num]].append(num)

        i = len(count2num)
        res = []
        while len(res)<k:
            i-=1
            if not count2num[i]:continue
            for j in range(len(count2num[i])):
                res.append(count2num[i][j])
        return res
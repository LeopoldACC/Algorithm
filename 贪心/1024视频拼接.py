class Solution:
    def videoStitching(self, clips, T: int):
        clips.sort()
        curs,cure,pree = float('inf'),0,0
        res = 0
        for i,[x,y] in enumerate(clips):
            if x>pree:
                pree = cure
                res+=1
            if x<=pree and y>cure:
                if y>=T:
                    return res+1
                cure = y
            
            print(pree,cure,res)
clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
T = 9
s = Solution()
s.videoStitching(clips,T)
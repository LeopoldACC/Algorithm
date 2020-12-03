class UndergroundSystem:

    def __init__(self):
        self.time = {}
        self.station = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.time[id] = [stationName,t]#self.station.get(id,[stationName,t])
        if stationName not in self.station:
            self.station[stationName] = {}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = t-self.time[id][1]
        start = self.time[id][0]
        self.station[start][stationName] = self.station[start].get(stationName,[0,0])
        self.station[start][stationName][0]+=time
        self.station[start][stationName][1]+=1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station[startStation][endStation][0]/self.station[startStation][endStation][1]
        


undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))   # // 返回 14.0。从 "Paradise"（时刻 8）到 "Cambridge"(时刻 22)的行程只有一趟
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))        # // 返回 11.0。总共有 2 躺从 "Leyton" 到 "Waterloo" 的行程，编号为 id=45 的乘客出发于 time=3 到达于 time=15，编号为 id=27 的乘客于 time=10 出发于 time=20 到达。所以平均时间为 ( (15-3) + (20-10) ) / 2 = 11.0
undergroundSystem.checkIn(10, "Leyton", 24)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))       #  // 返回 11.0
undergroundSystem.checkOut(10, "Waterloo", 38)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))      #  // 返回 12.0
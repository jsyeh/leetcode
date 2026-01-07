# LeetCode 1396. Design Underground System
# 實作「地下鐵」系統的 checkIn() checkOut() getAverageTime()
class UndergroundSystem:

    def __init__(self):
        self.checkInTime = {}  # 以乘客id為key，可查到 check in time
        self.totalTime = defaultdict(int)  # 以「start,end」為key
        self.totalN = defaultdict(int)  # 對應時間加總、人數

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInTime[id] = (stationName, t)        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t0 = self.checkInTime[id]
        self.totalTime[(startStation,stationName)] += (t-t0)
        self.totalN[(startStation,stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.totalTime[(startStation,endStation)] / self.totalN[(startStation,endStation)]
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

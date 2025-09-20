# LeetCode 3508. Implement Router
# 設計「資料結構」想模擬「網路封包」在Router傳送的過程：加封包、傳封包、統計某段時間的封包
class Router:

    def __init__(self, memoryLimit: int):  # 初始化「容量」及「資料結構
        self.limit = memoryLimit  # 容量限制
        self.packets = deque()  # 目前所有的封包，FIFO先進先出，所以用 deque()
        self.hashmap = set()  # 有哪些封包「在Router等待中」，用 hash set 快速找「重覆
        self.log = defaultdict(deque)  # 裡面記錄 self.log[目的地] 照時間的記錄
                    # 從 source 傳到 destination，時間是 timestamp
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool: 
        s = str(source) + ':' + str(destination) + ':' + str(timestamp)  # 把int變字串
        if s in self.hashmap: return False  # 如果是「重覆」的封包，就 return False
        self.hashmap.add(s)
        if len(self.packets) >= self.limit: # 超過 memoryLimit 就把「目前最舊」的刪掉
            self.forwardPacket()  # 刪掉 or 送出，結果一樣。所以共用 forward 函式
        self.packets.append(s)  # 加入這筆資料
        self.log[destination].append(timestamp)  # 記下這條log「對應的時間」
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.packets)==0: return []  # 沒有東西可以吐出來，好可憐，直接return
        s2 = self.packets.popleft()  # 吐掉「最早的」
        self.hashmap.remove(s2)  # 刪掉「最早的」對應的 hash set
        src, dst, t = list(map(int, s2.split(':')))  # 把字串「拆回原本的 3個整數」
        self.log[dst].popleft()  # forward 之後，就要吐掉、不在log裡記錄
        return src, dst, t  # 回傳「原本的 3個整數」

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        log = self.log[destination]  # 取出對應「目的地」的log記錄
        log1 = bisect_left(log, startTime)  # 利用 binary search 快速找到「對應的筆數」
        log2 = bisect_left(log, endTime+1)  # 為了包含「兩端」，需要+1
        return log2 - log1  # 「區間內有幾筆」= 兩個時間對應的log筆數相減


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

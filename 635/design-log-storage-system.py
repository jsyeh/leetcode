# LeetCode 635. Design Log Storage System
# put(id, timestamp字串) 記錄一堆 log 後，再用 retrieve(start,end,精細度)來找
# 精細度，是 retrieve 的 start與end 的精細範圍（更細的部分都不管）
class LogSystem:

    def __init__(self):
        self.log = SortedList()  # 利用 sortedcontainers.SortedList()

    def put(self, id: int, timestamp: str) -> None:
        self.log.add((timestamp, id))  # 以 timestamp 為主（排序）

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        print(self.log)
        a = start.split(':')  # 將時間 YYYY:MM:DD:hh:mm:ss 「斷開」
        start = []  # 將照精細度，放入 start
        for aa,g in zip(a,"Year:Month:Day:Hour:Minute:Second".split(':') ):
            start.append( aa.zfill(2) )  # YYYY不用補，其他都用0補齊2位
            if g==granularity: break  # 精確度到了，下面 binary search
        i = self.log.bisect_left((':'.join(start),0))
        b = end.split(':')  # 將時間 YYYY:MM:DD:hh:mm:ss 「斷開」
        end = []  # 將照精細度，放入 end
        for bb,g in zip(b,"Year:Month:Day:Hour:Minute:Second".split(':') ):
            end.append( bb.zfill(2) )  # YYYY不用補，其他都用0補齊2位
            if g==granularity: break  # 精確度到了，下面 binary search
        j = self.log.bisect_right((':'.join(end)+'z',inf)) # 加 'z' 保證墊底
        return [id for t,id in self.log[i:j]]  # i...j 對應的 id 取出來
        
# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)

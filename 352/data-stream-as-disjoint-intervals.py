# LeetCode 352. Data Stream as Disjoint Intervals
# 會一直給數字，數字相鄰時，區間要合併。getIntervals()要給全部的區間 
# 可使用 Union Find, 也就是利用 dict 查它的 root 是誰
# 每個數字，會對應一組「頭」，頭也會對應一組「範圍」。若有union就同時更新「頭」和「範圍」
class SummaryRanges:
    def find(self, x):  # 找出 x 對應的群組的「頭」
        if x not in self.head:  # 但若x從來都沒有設定群組
            return None  # 不存在（方便union()左右合併時，提早結束）
        if self.head[x] != x:  # 只要不一致，就一直更新下去
            self.head[x] = self.find(self.head[x])  # 讓 head[x]是最新的
        return self.head[x]  # 更新到一致時，就是答案

    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx==None or yy==None: return # 有1個無效、不用連起來，結束
        self.head[xx] = yy  # 連起來
        # 接下來把 interval 結合起來
        a = self.intervals[xx]  # x對應的區間「被合併」
        del self.intervals[xx]  # 被合併，就是「被消滅」
        b = self.intervals[yy]
        self.intervals[yy] = [min(a[0],b[0]), max(a[1],b[1])]

    def __init__(self):
        self.head = {}
        self.intervals = {}

    def addNum(self, value: int) -> None:
        if value in self.head: return  # 有存過資料，就不用再處理，提早結束
        # 沒有存過的話，先建資料，再嘗試合併（前後的數字）
        self.head[value] = value  # 自己是自己的頭
        self.intervals[value] = [value, value]  # 自己對自己
        self.union(value, value-1)  # 嘗試和前面合併
        self.union(value, value+1)  # 嘗試和後面合併

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.intervals.values())


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

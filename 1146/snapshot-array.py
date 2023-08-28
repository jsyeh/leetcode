# 設計的資料結構，是原長 lenght 的 list, 裡面有個自（長長的）list，記錄修改歷史
class SnapshotArray:

    def __init__(self, length: int):
        self.snapID = 0 # snapshot 的代碼
        self.history = [[[0,0]] for _ in range(length)]
        # 所以 history[index] 一格裡，有 [[snapID,val]]，會越來越長

    def set(self, index: int, val: int) -> None:
        self.history[index].append( [self.snapID, val] )

    def snap(self) -> int:
        self.snapID += 1
        return self.snapID - 1

    def get(self, index: int, snap_id: int) -> int:
        now = self.history[index] # now 是很長的 list，裡面存一堆 [t,val]
        left, right = 0, len(now)
        while left<right:
            mid = (left+right)//2
            if now[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid
        # print(now, left, snap_id)
        return now[left-1][1]

# case 3/75: ["SnapshotArray","set","set","set","snap","get","snap"]
# [[1],[0,4],[0,16],[0,13],[],[0,0],[]]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


# LeetCode 170. Two Sum III - Data structure design
# 設計資料結構： add(number) 可逐一加入數，
# 在 find(value) 時，會去查「目前」有沒有「2個數字」加起來是 value
# 最多呼叫 10^4 的 add() 和 find() 不能用暴力法去試
class TwoSum:

    def __init__(self):
        self.counter = Counter()

    def add(self, number: int) -> None:
        self.counter[number] += 1

    def find(self, value: int) -> bool:
        for c in self.counter:
            if value - c in self.counter:
                if value-c == c and self.counter[c]>1: return True
                if value-c != c: return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

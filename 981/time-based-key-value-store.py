# All the timestamps timestamp of set are strictly increasing.
# 所以set() 加入時，是照時間 sorted，在 get() 時，可用 binary search
class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([timestamp, value])
        else:
            self.map[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        timemap = self.map[key]
        left, right = 0, len(timemap)
        while left<right:
            mid = (left+right)//2
            if timemap[mid][0]==timestamp:
                return timemap[mid][1] # 找到了
            if timemap[mid][0]<timestamp:
                left = mid + 1
            else:
                right = mid
        if left==0: return ""
        return timemap[left-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

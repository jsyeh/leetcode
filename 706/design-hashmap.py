class MyHashMap:
    def __init__(self):
        self.table = {}    

    def put(self, key: int, value: int) -> None:
        self.table[key] = value

    def get(self, key: int) -> int:
        if key in self.table:
            return self.table[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.table:
            self.table.pop(key)

# 小心，不存在的 key 不能 remove/pop()
# case 1/36: ["MyHashMap","remove","get","put","put","put","get","put","put","put","put"]
# [[],[14],[4],[7,3],[11,1],[12,1],[7],[1,19],[0,3],[1,8],[2,6]]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# LeetCode 460. LFU Cache
# Least Frequently Used (LFU) cache 是「用太少的，優先清掉」
# 我參考 007623 的解法概念，使用 key2node 及 count2node 來管理node
# key 隨時間增加時，新的 node 對應的 count（累積使用數量）

class Node:  # 新增 Node 裡面有 count資訊
    def __init__(self, key, val, count): 
        self.key = key
        self.val = val
        self.count = count

class LFUCache:
    def __init__(self, capacity: int):  # 有容量限制
        self.capacity = capacity  # 記錄容量
        self.key2node = {}  # 指到答案的node

        self.minCount = 0  # 目前「用最少次」的數量，與下行合併使用
        self.count2node = defaultdict(OrderedDict)  # 這行重要
        # 利用 orderedDict 可用 popitem(last=False) 做出 FIFO

    def get(self, key: int) -> int:  # 也會把使用記錄 +1
        if key not in self.key2node:  # 找不到key
            return -1 # miss 時, 要 return -1
        node = self.key2node[key]  # 等下要回傳的「答案」，記得要先加1次
        del self.count2node[node.count][key] # 先拔掉舊的，因等下會要更新
        if not self.count2node[node.count]:  # 若拔光時
            del self.count2node[node.count]  # count 對應 空的 OrderedDict 也要拔掉
        
        # 拔掉1個，順便檢查 self.minCount 這層要不要變動
        if not self.count2node[self.minCount]: # 若這層變成空的
            self.minCount += 1  # 就更新到下一層（因下面會「加1次」後補回）

        node.count += 1  # 加1次使用的記錄
        self.count2node[node.count][key] = node  # 改放到樓上
        return node.val  # 更新完資料結構，總算可以 return 答案了

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:  # 若有舊的記錄
            self.key2node[key].val = value  # 改成新的值
            self.get(key)  # 使用記錄 +1
            return
        # 以下要加「新」的記錄。加之前，先吐1筆「舊的、用最少的」
        if len(self.key2node) == self.capacity: # 容量將超過，吐1個
            k, o = self.count2node[self.minCount].popitem(last=False)
            del self.key2node[k]
        # 以下為新資料「新建」資料結構的記錄
        node = Node(key,value,1)  # 新資料放在「只用1次」區
        self.key2node[key] = node
        self.count2node[1][key] = node
        self.minCount = 1 # 「最少使用的次數」回歸回1筆

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# insert() 重覆就 false
# remove() 不存在就 false
# getRandom() 就平均挑1個
# 速度都要O(1)，最多 2*10^5 次操作
# 本來我想用 set() 但不知怎麼亂數取出某個值
# 查到 SortedSet() 可用，但 remove() 及 [i] 要 O(log(n)) 不合規定。
# https://grantjenks.com/docs/sortedcontainers/sortedset.html
from sortedcontainers import SortedSet
class RandomizedSet:

    def __init__(self):
        self.pool = SortedSet()
        self.size = 0
    def insert(self, val: int) -> bool:
        if val in self.pool: return False
        self.pool.add(val)
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pool: return False
        self.pool.remove(val) # 文件說這個耗時O(log(n))
        self.size -= 1 # 所以其實不合規定
        return True

    def getRandom(self) -> int:
        i = randrange(self.size)
        return self.pool[i] # 文件說這個耗時O(log(n))
        # 所以其實不合規定

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

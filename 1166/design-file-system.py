# LeetCode 1166. Design File System
# 設計 createPath() 及 get() 可使用 Hash Table 來實作
class FileSystem:

    def __init__(self):
        self.table = {}  # Hash Table 用來對應「目錄」及 value
        self.table['/'] = 0  # 要先有「根目錄」才能長出其他目錄

    def createPath(self, path: str, value: int) -> bool:
        if path in self.table:  # 目錄已存在
            return False  # 不能重覆，失敗
        d = path.split('/')  # 把 path 的每段目錄名「切開」
        if len(d[:-1])!=1 and '/'.join(d[:-1]) not in self.table:
            # len(d[:-1]) 有可能是根目錄，會切出 [''] 對應長度是1
            # parent 目錄 d[:-1] 必須要存在，所以不存在的話，就失敗
            return False  # parent 目錄不存在
        self.table[path] = value  # 有 parent 目錄，並且本身不存在，就可存值
        return True  # 成功，非常好


    def get(self, path: str) -> int:
        if path not in self.table:  # 目錄不存在
            return -1  # 就失敗
        return self.table[path]  # 存在的話，可成功放值
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

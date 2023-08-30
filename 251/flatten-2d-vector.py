# 小心，2D 可能長度都不同。
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.i, self.j = 0, 0
        self.checkValid()

    def checkValid(self):
        # 這是專門對付 [[],[],[],[1]] 這種怪狀況
        # ["Vector2D","hasNext","next","hasNext"]
        # [[[[],[],[],[1]]], [],[],[]]
        while self.i < len(self.vec) and self.j >= len(self.vec[self.i]):
            self.i += 1
            self.j = 0

    def next(self) -> int:
        # self.checkValid()
        i, j = self.i, self.j
        self.j += 1 # 移到下一格待命
        self.checkValid()
        return self.vec[i][j]

    def hasNext(self) -> bool:
        if self.i < len(self.vec) - 1:
            return True
        if self.i < len(self.vec) and self.j < len(self.vec[self.i]):
            return True
        return False

# case 2/18: ["Vector2D","hasNext"]
# [[[]],[]] 小心空的部分，要加 if self.i<len(self.vec) 保護
# case 8/18: ["Vector2D","hasNext","next","hasNext"]
# [[[[1],[]]],[],[],[]]
# case 7/18: ["Vector2D","hasNext","next","hasNext"]
# [[[[],[3]]],[],[],[]]

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()

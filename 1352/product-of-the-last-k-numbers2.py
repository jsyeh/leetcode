# LeetCode 1352. Product of the Last K Numbers
# 資料結構題：add()會在後面加數字， getProduct(k) 回傳「最後k個數乘起來」的值
# 可用 running product 的概念來解，即事先存「有一堆數字相乘」的結果。
# 但是「只要中間摻了1個0」整個就變成0，所以「遇到0就新的開始」重頭處理。
class ProductOfNumbers:
    def __init__(self):
        self.nonZero = 0  # 目前「後面數回來」，有幾個「非零」的項
        self.run = [1]  # 邊跑邊乘，所以最後k筆相乘，就 run[-1] // run[-k-1]
    def add(self, num: int) -> None:
        if num==0:  # 不幸碰到0，有0摻進來，就要「從新開始」
            self.nonZero = 0  # 目前「後面數回來」，有0個「非零」的項
            self.run = [1]  # 重新來過
        else:
            self.nonZero += 1  # 多1個「非零」的項
            self.run.append( self.run[-1] * num )
    def getProduct(self, k: int) -> int:
        if self.nonZero < k: return 0  # 「非零」的項「不夠」，就變成0
        return self.run[-1]  // self.run[-1-k]  # 最後 k 項和，就將距離 k 的 2數相除

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

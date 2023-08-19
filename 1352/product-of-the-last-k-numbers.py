# 題目說不會超過 32-bit integer，所以可用 running product
# 但是，遇到0就沒救了
class ProductOfNumbers:

    def __init__(self):
        self.runProduct = [1] # 乘法基礎元素1
        self.nums = [1] # 想像最前面有個保護的基礎元素1
        self.runZeros = [0] # 用來記錄「累積幾個0」
        self.N = 1

    def add(self, num: int) -> None:
        N = self.N
        self.nums.append(num) # 這個好像不會用到
        if num == 0: # 糟糕，有0滲進來了
            self.runZeros.append(self.runZeros[N-1]+1)
            self.runProduct.append(1) # 又從頭來過
        else:
            self.runZeros.append(self.runZeros[N-1])
            self.runProduct.append(self.runProduct[N-1]*num)
        self.N += 1
    def getProduct(self, k: int) -> int:
        N = self.N
        if self.runZeros[N-1] - self.runZeros[N-1-k] > 0:
            return 0 # 有1個以上的0摻在裡面
        return self.runProduct[self.N-1] // self.runProduct[self.N-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

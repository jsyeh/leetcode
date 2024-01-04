# self-dividing number 是「每一位,都可整數自己」的數
# ex. 128 是, 因 128 可被 1, 2, 8 整除
# 題目列出範圍, 請把裡面全部的數都列出來
class Solution:
    @cache # 利用 cache 想要快一點, 因為會重覆問多次
    def isSelfDividing(self, n):
        n2 = n
        while n>0:
            # 遇到0一定錯, 不能整除也是錯
            if n%10==0 or n2%(n%10)!=0: return False
            n //= 10
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1): # 右邊界要包含, 所以+1
            if self.isSelfDividing(i): ans.append(i)
        return ans

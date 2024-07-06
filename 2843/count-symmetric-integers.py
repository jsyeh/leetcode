# LeetCode 2843. Count Symmetric Integers
# 如果數字「前半」加起來==「後半」加起來，就合格 ex. 1203 1+2==0+3
# 問 low...high 之間，有幾個合格的數
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def helper(n):
            L = len(str(n)) # 先知道數字n的位數/長度
            if L%2==1: return False # 奇數的話，就失敗
            left, right = 0, 0 # 分別統計左半、右半的數字和
            for i in range(L//2): # 左半先剝皮
                left += n % 10
                n //= 10
            for i in range(L//2): # 右半再剝皮
                right += n %10
                n //= 10
            return left==right # 看長度是否相同
        ans = 0
        for i in range(low, high+1): # 左右都包含
            if helper(i): ans += 1 # 查看i是否合格，再+1
        return ans

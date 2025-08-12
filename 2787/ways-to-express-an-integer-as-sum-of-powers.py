# LeetCode 2787. Ways to Express an Integer as Sum of Powers
# a^x 叫 a的x次方，把一堆加起來，有名的是 3^2 + 4^2 == 5^2 剛好是畢氏定理的例子。
# 題目給你 x 次方，給你目標數字 n 問你「有幾種（不同的整數的x次方）相加，可組合出n的方法」
# 因為「數字都不同」把它看成慢慢變大，可用「函式呼叫函式」的 Dynamic Programming 可解
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        @cache  # 把「大問題」拆解成「小問題」剛好可解
        def helper(i, n):  # 使用1^x 到 i^x 有幾種方法「組出n」
            # print('i', i, 'n', n)  # 為了 debug 可印出參數，看它呼叫時的變化
            if n==0: return 1  # 終止條件：剛好湊成功
            if n<0: return 0  # 終止條件：用太多了，失敗
            if i<=0: return 0  # 終止條件：走到太超過了，失敗
            if n-i**x<0:  # 如果「使用i」扣掉 i^x 後，會變成負數，就不夠用，不能再叫用下去
                return helper(i-1, n)  # 函式呼叫函式，只能「避開i」，不能「使用i」
            return helper(i-1, n) + helper(i-1, n-i**x)  # 函式呼叫函式
            # 左邊helper()是「避開i」 右邊helper()是「使用i」
        return helper(n, n) % (10**9+7) # 函式呼叫函式

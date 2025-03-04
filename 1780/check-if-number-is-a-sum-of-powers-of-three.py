# LeetCode 1780. Check if Number is a Sum of Powers of Three
# n 能不能用一堆 3 的次方「加起來」。Hint 1 10^6 約 3^16 可用
# Hint 2 建議「三進位」，只要 n 能變成「三進位」表示法，就一定成功！
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:  # 利用「剝皮法」把數字「每次除3」
            if n % 3 == 2:  # 可以是 0, 1, 不能是 2
                return False  # 如果是 2 就是失敗
            n //= 3  # 剝皮法
        return True  # 順利剝皮完成，便是可以用「三進位」表示


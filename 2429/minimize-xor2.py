# LeetCode 2429. Minimize XOR
# 兩數 num1 num2 請找 x （與num2有相同的0和1）使 x XOR num1 最小
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a, b = bin(num1).count('1'), bin(num2).count('1') 
        # 把數字，變 binary 字串，再「數」有幾個'1'，因為目標是要有「相同的1」

        ans = num1  # 希望 ans XOR num1 最小（最小的極限是 num1 XOR num1 會得到 0）
        for i in range(32):  # 32 位元的整數「從低到高位」處理
            if a>b and (ans & (1<<i) != 0):  # 如果兩組的 1 不同，目前 ans 的 '1' 過多，把「低位數」的1「去掉」
                ans ^= (1<<i)
                a -= 1  # 現在 ans 裡，少掉1個1
            if a<b and (ans & (1<<i) == 0):  # 目前 ans 的 '1' 不夠多，也是放在「低位數」
                ans ^= (1<<i)
                a += 1  # 現在 ans 裡，增加1個1
        return ans

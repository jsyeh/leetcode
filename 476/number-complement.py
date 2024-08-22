# LeetCode 476. Number Complement 計算機概論「二進位」的補數（0變1、1變0）
# 會有很多種方法來解決問題。簡單觀察，發現 7(111) - 5(101) 得到 2(010)
# 所以使用減法，把「一堆1」減掉 num 剩下就是答案。可用「2的n次方」減1，得到「一堆1」
# 但「一堆1」 要幾個1呢？可慢慢試，多試幾次，等到位數「足夠」為止。
class Solution:
    def findComplement(self, num: int) -> int:
        now = 2  # 要做出2的倍數
        while True: 
            # if num<now: return (now-1) - num # 使用減法
            if num < now: return (now-1) ^ num # 使用 XOR 更適合
            now *= 2

# LeetCode 693. Binary Number with Alternating Bits
# 將整數 n 變成二進位字串，問「相鄰的bit」是否 0 1 交錯
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)  # 先把 n 變成二進位字串 '0bXXXX'
        for i in range(2, len(bits)-1):  # 避開前面的 '0b'
            if bits[i] == bits[i+1]:  # 相鄰竟然相同
                return False  # 就失敗
        return True  # 順利檢測完，成功

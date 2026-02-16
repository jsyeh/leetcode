# LeetCode 190. Reverse Bits
# 將整數 n 以二進位表示後，將 32 bits 全部反過來的整數
class Solution:
    def reverseBits(self, n: int) -> int:
        # 方法1: 變成二進位字串、去除'0b'，反過來、接成字串，後面補'0'到32位元，再整數
        bits = bin(n)  # 利用 bin() 將整數變成字串 '0b' 開頭的二進位字串
        return int(''.join(reversed(bits[2:])) + '0'*(32-len(bits)+2), 2)

        # 方法2: 變成二進位字串、去除'0b'，補齊'0'變成32位、反過來，接成字串，轉回整數
        bits = bin(n)[2:].zfill(32)
        return int(''.join(reversed(bits)), 2)

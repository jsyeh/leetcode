# LeetCode 190. Reverse Bits
# 將整數 n 以二進位表示後，將 32 bits 全部反過來的整數
class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)  # 利用 bin() 將整數變成字串 '0b' 開頭的二進位字串
        # 用以下 print() 講解程式執行的過程，以 n = 4 為例
        print(bits, '二進字串')  # bits = bin(4) 會得到 '0b100'
        print(bits[2:], '去除開頭')  # 去除開頭的 '0b' 會得到二進位的 '100'
        反過來 = ''.join(list(reversed(bits[2:])))  # Python 中文當變數名
        print(反過來, '反過來')  # 將 '100' 反過來, 變成 '001' 不過沒有補齊 32位元
        補齊32位元 = ''.join(list(reversed(bits[2:]))) + '0' * (32-len(bits)+2)
        print(補齊32位元, '補齊32位元')  # '001' + '00000000000000000000000000000'
        前面補0b = '0b' + ''.join(list(reversed(bits[2:]))) + '0'*(32-len(bits)+2)
        print(前面補0b, '前面補0b')  # '0b' + '001' + '00000000000000000000000000000'
        # 最後的答案, 要將「二進位的字串」表示的整數
        return int('0b' + ''.join(list(reversed(bits[2:]))) + '0'*(32-len(bits)+2), 2)

# LeetCode 1545. Find Kth Bit in Nth Binary String
# 字串產生規則：新字串 = 舊字串 + "1" + 左右反過來(01相反(舊字串))
# n=1時，字串是 "0" 長度1
# n=2時，字串是 "011" 長度3
# n=3時，字串是 "0111001" 長度7
# n=4時，字串是 "011100110110001" 長度15
# 給你 n 及 k 找到字串 n 的第 k 個字，因為長度會倍增，要找到公式
class Solution:  # 利用「函式呼叫函式」問更簡單的問題
    def findKthBit(self, n: int, k: int) -> str:
        table = {"0":"1", "1":"0"}  # 對照表，會01相反
        def helper(n, k):  # 利用「函式呼叫函式」拆解問題後，找答案
            if n==1: return "0"  # 最基礎的字串
            L = 2**n - 1  # 字串長度公式：2的n次方 - 1
            MID = 2**(n-1)  # 中間的數，要小心 1-index 不是 0-index
            if k < MID: return helper(n-1, k)  # 左半  
            elif k == MID: return "1"  # 中間的1
            else: return table[ helper(n-1, L-k+1) ]  # 右半，要折一半、反過來
        return helper(n, k)  # 「函式呼叫函式」去問答案

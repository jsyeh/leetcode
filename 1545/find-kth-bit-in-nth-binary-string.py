# LeetCode 1545. Find Kth Bit in Nth Binary String
# 字串規則：新字串 = 舊字串 + '1' + 右半邊反過來、再倒反的字串
# 字串1 是 "0"   最早的條件
# 字串1 是 "011"  "0" + 中間"1" + 右半邊變成1
# 字串2 是 "0111001" "011" + 中間"1" + (右半邊：反過來"100"再倒反 "001")
# 字串3 是 "011100110110001" (右半邊：反過來"1000110"再倒反 "1001110")
# 問「字串n」的第k個字母。因為 k 可能超級大 2^20-1 所以不能真的產生字串
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # 可找出 k 對應的「公式」，或利用「函式呼叫函式」問更簡單的問題
        if n==1: return "0"  # 終止、結束條件，本題 1-index 不是 0-index
        total = 2**n - 1  # 目前「總長度」公式: 2^n -1
        half = 2**(n-1)  # 正中間的數（的index)
        if k == half: return "1"  # 剛好是正中間的那個1
        if k < half: return self.findKthBit(n-1, k)  # 左半邊，函式呼叫函式
        else:  # 右半邊，比較麻煩，要反過來、再倒反
            ans = self.findKthBit(n-1, total-k+1) # 左邊數k，即右邊數 total-k+1 (1-index)
            if ans=="1": return "0"
            else: return "1"

# LeetCode 650. 2 Keys Keyboard 只有「複製、貼上」的鍵盤。
# 一開始有1個字母，你可敲 CopyAll 複製，再敲 Paste 貼上，敲2個鍵，就變成2字母。
# 敲100個鍵，會變100個字母，不過這樣太慢了，有時候可重新「CopyAll複製」再貼，
# 可敲更少的鍵，完成任務。請你寫程式，看n個字母，最少要敲幾次鍵。
# 這類型的題目，是典型的 DP (Dynamic Programming動態規劃) 的題目：
# 可建個表格，table[i] 表示比較小的問題，再更新表格，看有沒有更好的答案。
# 以本題來說，建出 table 長度為 (n+1) 格，那就有 table[0]...table[n] 要填。
# 一開始 table[i] 先設成 i，因最簡單的敲法，就 Ctrl-C 之後瘋狂 Ctrl-V 。
# 不過有時候有更好的答案：如果 i 可以被某個數 k 整除，那就有捷徑，
# 可以直接從 table[k] 經過 i//k 步，複製出 table[i] 的結果。
class Solution:
    def minSteps(self, n: int) -> int:
        table = [0]*(n+1)
        for i in range(2,n+1):
            table[i] = i
# 調整裡面的 for k 迴圈，從一半開始退，程式可快4倍，心情很愉快 ❤
            for k in range(i//2, 2, -1):
                if i%k==0: 
                    table[i] = table[k] + i//k
                    break
        return table[n]

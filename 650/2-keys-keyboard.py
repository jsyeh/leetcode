# table[i] : 第i步能做到的字數，table[n]是答案。
# 第1步是copy,最笨的方法是Ctrl-V一直做，所以table[i]=i
# 它是問要到達n個字母，最少要做幾步。要剛好n個字母，不能多不能少
# 接著倒過來更新，看前一步能否整除。
# 若剛好是某個整除，可用整除的數字Ctrl-V貼達目標，步數便是 dp[i] = dp[j] + int(i/j) ，
class Solution:
    def minSteps(self, n: int) -> int:
        table = [0]*(n+1) # table[i] 「剛好」要有 i 個字母，要幾步做到
        # 所以剛好要有 1 個字母時，0步便能做到，因為現成就是1個字母
        for i in range(2, n+1): # 想知道 table[2]...table[n] 的值
            table[i] = i # 基本款，第1步copy, 接下來就 paste... 所以總步數剛好是i

            for k in range(i-1, 2, -1): # 倒過來的迴圈，查是否有「一步登天」的巧合
                if i%k==0: # 剛好可以整除，表示可以 paste到這個值
                    table[i] = table[k] + int(i/k) # 太好了，更新，更快達到
                    # 也就是 k字母，再貼 i/k-1次，便達到「剛好」i個字母
                    # Q: 在 table[k]後，有copy all 嗎？好像沒有耶。。。
                    # A: 因為本身有1倍，剛好對應1次動作copy all，所以還是 + int(i/k)
                    break # 因只有copy/paste，能湊到就萬幸了
        return table[n]

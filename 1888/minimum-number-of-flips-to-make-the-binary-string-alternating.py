# LeetCode 1888. Minimum Number of Flips to Make the Binary String Alternating
# 可先將「開頭的字母移到最後面」多次（類似rotate的意思）
# 請問flip翻轉（某字母0、1交換）幾次後，字串可變成0、1交錯
class Solution:
    def minFlips(self, s: str) -> int:
        N = len(s)  # 原本字串的長度，也是我們 sliding window 的大小
        s = s + s  # 變成長度「兩倍」的字串，便解決 rotate 的問題
        ans0 = ans1 = 0  # 目標「交錯字串」可以0開始、可以1開始
        for i in range(N*2):  # 針對「兩倍」的字串，裡面「長度N」的 sliding window
            # 右邊的頭，往右更新（加上「要付出的代價」）
            if i%2==0:  # 偶數位數
                if s[i]=='1' : ans0 += 1  # 要付出的代價
                else: ans1 += 1  # 要付出的代價
            else: # 奇數位數
                if s[i]=='0': ans0 += 1  # 要付出的代價
                else: ans1 += 1  # 要付出的代價
            if i==N-1: ans = min(ans0, ans1)  # 剛好湊齊「長度N」，找到第1組答案
            # 左邊的尾巴，往右更新（扣掉「要付出的代價」）
            if i-N >= 0:  # 過半，要扣掉 i-N 對應結果
                if (i-N)%2==0:  # 偶數位數
                    if s[i-N]=='1': ans0 -= 1  # 扣掉「要付出的代價」
                    else: ans1 -= 1  # 扣掉「要付出的代價」
                else:
                    if s[i-N]=='0': ans0 -= 1  # 扣掉「要付出的代價」
                    else: ans1 -= 1  # 扣掉「要付出的代價」
                ans = min(ans, ans0, ans1)  # 更新答案
        return ans

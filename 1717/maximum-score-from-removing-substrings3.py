# LeetCode 1717. Maximum Score From Removing Substrings
# 最粗暴的解法，利用 if 判斷，分成2大群，總共有4大塊 while 迴圈
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s = list(s)  # 把字串變成 list 便能在之後用 s[i] = s[j] 改變內容
        ans = 0
        N = len(s)
        i, j = 0, 1  # 左手i 右手j
        if x > y:  # 如果 'ab' 的價值比較高，就先消掉 'ab'
            while j<N:
                if i>=0 and s[i]+s[j] == 'ab': # 可以組成 'ab'
                    ans = ans + x  # 消掉，可以得到 x 分
                    i = i - 1  # 消掉後，左邊左移1格
                    j = j + 1  # 消掉後，右邊右移1格，左右的中間多2個空格
                else:  # 無法消掉的話
                    i = i + 1  # 左邊保留，移1格
                    s[i] = s[j]  # 把右邊移到左邊，便能讓「左邊接成連續」
                    j = j + 1  # 右邊往右持續探索
            N = i + 1  # 目前剩下 N 個字母
            i, j = 0, 1  # 一樣 左手i 右手j 重新開始
            while j<N:
                if i>=0 and s[i]+s[j] == 'ba':
                    ans = ans + y
                    i = i - 1
                    j = j + 1
                else:
                    i = i + 1
                    s[i] = s[j]
                    j = j + 1
            return ans
        else:  # 如果 'ba' 價值比較高，就先做 'ba'
            while j<N:
                if i>=0 and s[i]+s[j] == 'ba':
                    ans = ans + y
                    i = i - 1
                    j = j + 1
                else:
                    i = i + 1
                    s[i] = s[j]
                    j = j + 1
            N = i+1
            i, j = 0, 1
            while j<N:
                if i>=0 and s[i]+s[j] == 'ab':
                    ans = ans + x
                    i = i - 1
                    j = j + 1
                else:
                    i = i + 1
                    s[i] = s[j]
                    j = j + 1
            return ans

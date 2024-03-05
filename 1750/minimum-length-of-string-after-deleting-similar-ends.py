# 化簡步驟：prefix字首字母要相同，suffix字尾字母要相同，不能交錯。
# 再把字首、字尾一起消掉。問可以消掉多少、變多短。
# 看起來簡單，但字串s長度 10^5很大，最好一邊讀、一邊消
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s)-1 # 待消的可能候選人
        while left<=right:
            if s[left]==s[right] and left!=right: # 相同、可消，且左右各1格以上（不重疊）
                now = s[left] # 現在能消的候選人
                while left<=right and s[left]==now:
                    left += 1 # 左界往右移，消掉1個字母
                while left<=right and s[right]==now:
                    right -= 1 # 右界往左移，消掉1個字母
            else:
                break    
        return right - left + 1
# case 96/100: "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"

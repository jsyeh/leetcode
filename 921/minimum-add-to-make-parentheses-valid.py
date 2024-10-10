# LeetCode 921. Minimum Add to Make Parentheses Valid
# 給一堆圓括號，加幾個括號後，能讓「括號對應正確」？
# 和昨天題目 1963 類似，數括號，如果不夠時 +1。結束時，補足depth深度
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0  
        depth = 0
        for c in s:  # 逐個括號分析
            if c=='(':  # 遇到上括號，多一層
                depth += 1
            else:  # 遇到下括號，應該要扣一層
                if depth>0:  # 括號足夠，很好，扣一層
                    depth -= 1
                else:  # 但括號不夠的話
                    ans += 1  # 需要 add 加1個括號
        return ans + depth  # 最後答案，要再加上「多出來的depth」要補下括號

# LeetCode 1653. Minimum Deletions to Make String Balanced
# 'a'只能在左邊、'b'只能在右邊。你要刪掉幾個字母，才能做到？
# 可用迴圈逐一檢查：「左邊有幾個'b'、右邊有幾個'a'」就知道要刪掉幾個字母
class Solution:
    def minimumDeletions(self, s: str) -> int:
        countA = s.count('a')  # 先知道「總共有幾個'a'」對應「右邊有幾個'a'」
        countB = 0  # 等一下用迴圈，了解s[i]「左邊有幾個'b'、右邊有幾個'a'」
        ans = countB + countA  # 要刪的字母：「左邊有幾個'b'、右邊有幾個'a'」
        for c in s:  # 用迴圈逐一檢查, c = s[i] 如果當 a b 分隔線
            if c=='a': countA -= 1  # 讓右邊有幾個'a'變少
            if c=='b': countB += 1  # 讓左邊有幾個'b'增加
            ans = min(ans, countB + countA)  # 現在的分隔線，要刪掉幾個字母
        return ans

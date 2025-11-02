# LeetCode 3407. Substring Matching Pattern
# p 字串裡的「*星號」可塞入「任何數量的字母」，s字串裡是否容得下 p字串？
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        part1, part2 = p.split('*')  # 先把 p 字串，斷成「前半」「後半」兩段
        i = s.find(part1)  # 先找「前半」
        if i==-1: return False  # 找不到，就失敗
        i2 = s[i+len(part1):].find(part2)   # 再找「後半」
        return i2 != -1  # -1找不到，就失敗。（不是-1）找得到，就成功。

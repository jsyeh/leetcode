# 又是開心的 Easy 題，果然6月1日是好的開始。
# 今天的挑戰題，是要算一下「字串」對應的分數。
# 把「相鄰的字母的ASCII值的差」，全部加起來，就是答案了
class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0  # 迴圈前面 ans 是0
        for i in range(len(s)-1):  # 種樹問題：n個樹，間隔n-1
            # 迴圈中間，更新 ans
            ans += abs(ord(s[i+1]) - ord(s[i]))  # 相減的距離
        return ans  # 迴圈後面，把答案拿來用

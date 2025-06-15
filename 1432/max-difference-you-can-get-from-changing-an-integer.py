# LeetCode 1432. Max Difference You Can Get From Changing an Integer
# num 數字裡，可挑 0...9 其中一個數字x，換成 0...9的數字y
# 能做出的「最大數」減「最小數」會是多少呢？（不能有 leading zero)
class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)  # 用字串處理，方便 replace() 變換字母
        ansMax, ansMin = -inf, inf  # 技巧找最大值，先設成最小值
        for x in "0123456789":  # 挑0...9其中一個數 x
            for y in "0123456789":  # 挑另一個數 y
                num2 = num.replace(x,y)  # 用取串取代，將 x 變成 y
                if num2[0] == '0': continue  # leading zero
                ansMax = max(ansMax, int(num2))  # 再取 max()
                ansMin = min(ansMin, int(num2))  # 再取 min()
        return ansMax - ansMin  # 「最大數」減「最小數」，得到答案

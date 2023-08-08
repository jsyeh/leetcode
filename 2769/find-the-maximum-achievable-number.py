# 找出最大的答案，每次+1或-1
# 其實就把 num + t*2 應該就可以了
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t*2

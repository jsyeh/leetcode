# LeetCode 2578. Split With Minimum Sum
# 把數字，分成2個數，希望數字「加起來」最小
class Solution:
    def splitNum(self, num: int) -> int:
        num = sorted(list(str(num)))  # 把數字「小到大」排好
        num = str(int(''.join(num)))  # 再把 leading zero 也刪掉
        if len(num)==1: return int(num)  # 如果只有1位數，就直接當答案
        return int(num[0::2]) + int(num[1::2])  # 可分成2個數

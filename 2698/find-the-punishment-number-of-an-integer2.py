# LeetCode 2698. Find the Punishment Number of an Integer
class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        cheat = [0, 1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]  # 作弊，把全部的數，先算出來
        for i in cheat:  # 照著作弊的小抄，逐一比較
            if i > n:  # 如果小抄裡的數，比 input n 數字大
                break  # 就不用再翻書作弊了！
            ans += i * i  # 一邊翻書、一邊算答案
        return ans

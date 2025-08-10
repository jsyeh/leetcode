# LeetCode 869. Reordered Power of 2
# 把數字的十進位「位數」調整順序，變成 2 的次方 ex. 46 變成 64
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 先把答案 1,2,4,8,16,32,..,2的30次方 都變成「小到大排好」的字串
        possible = set()  # 可能的數字「小到大排好」的字串
        num = 1  # 從 1 開始，一直乘 2 一直乘 2
        for i in range(31):  # 從 2的0次方 ... 2的30次方
            # 數字變成「小到大排好」的字串
            possible.add(''.join(sorted(str(num))))
            num = num * 2  # 一直乘 2 一直乘 2
        digits = ''.join(sorted(str(n)))  # 數字變成「小到大排好」的字串
        if digits in possible:
            return True  # 有可能重新排列出來，成功
        return False  # 無法重新排列出來，失敗

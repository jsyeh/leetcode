# LeetCode 1323. Maximum 69 Number
# 你可以把 num 裡「其中一個6換成9」希望變「最大」
# 作法：遇到第一個出現的6，把它換成9，就可以了
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))  # 先變成「可修改」的字母的list
        for i in range(len(num)):  # 巡字母
            if num[i]=='6':  # 找到第一個出現的6
                num[i] = '9'  # 把它換成9
                break  # 就可以結束了
        return int(''.join(num))  # 把字母「接」成字串，再轉成整數

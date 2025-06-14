# LeetCode 2566. Maximum Difference by Remapping a Digit
# num 不同位數，把 0...9 挑一個數，全部換成另一個數
# 把能做出來的最大 vs. 能做出來的最小，兩個相減，得到答案。
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)  # 把「數字」變「字串」方便分析
        tableBig = {str(i):i for i in range(10)}  # 有兩種「對照表」
        tableSmall = {str(i):i for i in range(10)}  # 「字母」變「數字」
        foundBig, foundSmall = False, False  # 一開始，還沒找到「要換哪一個數」
        ansBig, ansSmall = 0, 0  # 把換算出來的結果，累積到答案裡
        for c in s:  # 逐位數分析
            if not foundBig and c != '9':  # 第1個不是'9'的字母
                foundBig = True  # 找到囉！
                tableBig[c] = 9  # 把它換成 9
            if not foundSmall and c != '0':  # 第1個不是'0'的字母
                foundSmall = True  # 找到囉！
                tableSmall[c] = 0  # 把它換成 0
            # 上面建好「對照表」，下面就直接像「剝皮法」那樣「組合出答案」 
            ansBig = ansBig * 10 + tableBig[c]
            ansSmall = ansSmall * 10 + tableSmall[c]
        return ansBig - ansSmall  # 大數 - 小數

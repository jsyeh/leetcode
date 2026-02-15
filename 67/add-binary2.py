# LeetCode 67. Add Binary
# a 和 b 是二進位的字串，找到「二進位加法」後的字串
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 字串很長，不能轉成整數。先變成list，便能用 pop()取出最右邊位數
        a, b = list(a), list(b)
        ans = []  # 將從「低位」到「高位」塞入答案，之後要再 reversed()
        carry = 0  # 進位的部分
        while a or b:  # 只要還有數在
            if a: carry += int(a.pop())  # 若 a 還有，將最小位變整數
            if b: carry += int(b.pop())  # 若 b 還有，將最小位變整數
            ans.append(carry%2)  # 看這個位數「要存入1還是存入0」
            carry = carry // 2  # 更高位數的「進位」部分
        if carry: ans.append(carry)  # 離開迴圈後，若還有「進位」就再存入
        return ''.join(list(map(str, reversed(ans) )))
# 最後這行有點噁心：先reversed()倒過來，再逐一轉成字母，再接成1個大字串

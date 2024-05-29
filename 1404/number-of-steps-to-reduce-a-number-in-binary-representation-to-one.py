# LeetCode 1404. Number of Steps to Reduce a Number in Binary Representation to One
# 題目用二進位字串，來表達「很大的整數」然後照規則：偶數除2、奇數加1 問要做幾步，會變成1
# 這題是 Medium 中等題，不過使用 Python 的人會覺得「蛤？這有很難嗎？轉成整數就好了吧」
# 那是因為 Python 有「超大整數」的支援。其他語言的人，可能要「自己實作加法&進位」慢慢算。
class Solution:
    def numSteps(self, s: str) -> int:
        now = int(s,2)  # 利用 Python 內建功能，從2進位字串，變成「超大整數」
        ans = 0  # 答案走幾步會變成1
        while now!=1:  # 迴圈一直做，直到變成1為止（不是1，就一直做）
            if now%2==1: now = now + 1  # 奇數，就 +1
            else: now = now // 2  # 偶數，就除2 。整數除法要用2個斜線
            ans += 1  # 答案又多走了1步
        return ans

# 這題只是除法取餘數，不過負數會發生問題。
# 所以就先轉成正數，算好後再加負號即可。
# 接著在 Testcase 試 7 3 -7 3 7 -3 -7 -3 都試過即可
# 特別邊界： -2147483648 -1
# 特別邊界： -2147483648 1
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend*divisor<0: # 如果是負的，要例外處理
            ans = -(-dividend//divisor)
        else: # 簡單的部分
            ans = dividend // divisor
        # 下面是題目額外要求：不能太大、不能太小
        if ans > 2**31-1:
            ans = 2**31-1
        if ans < -2**31:
            ans = -2**31
        return ans
# case 993/994: -2147483648 -1 竟然要求輸出 2147483647
# 可是它應該是 2147483648 啊？
# 原來題目有說明 「 if the quotient is strictly greater than 231 - 1, then return 231 - 1」
# 所以要再 -1

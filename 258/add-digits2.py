# LeetCode 258. Add Digits
# 利用「剝皮法」將每個位數「加起來」，利用「函式呼叫函式」做到結束。
class Solution:
    def addDigits(self, num: int) -> int:
        if num<10: return num  # 終止條件，確認算完了

        ans = 0  # 新的答案，累積「每個位數的值」
        while num>0:  # 簡單的「剝皮法」迴圈
            ans += num % 10
            num //= 10
        return self.addDigits(ans)  # 利用「函式呼叫函式」繼續做

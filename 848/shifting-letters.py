# 字串長度 <= 10^5, 而真的 shift 會做「這麼多次」*這麼多次
# 所以不能用模擬法。可以試試（倒過來的） prefix sum 再用 %26 來找到對應的數字
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        N = len(s)
        for i in range(N-2,-1,-1): # 將 shifts 變成類似 prefix sum
            shifts[i] += shifts[i+1]

        # 現在的 shifts[i] 的值，是「模擬後」累積的結果，可拿來算答案了
        ans = [c for c in s] # 先用 list 來表示原本的值
        for i in range(N): # 針對每個字母，算位積量
            # 先變成 ASCII 值，再轉成「與'a'的距離」，再shifts[i]後，再取%
            ans[i] = (ord(ans[i]) - ord('a') + shifts[i]) % 26
            ans[i] = chr(ans[i]+ord('a')) # 再變回字母
        return ''.join(ans)

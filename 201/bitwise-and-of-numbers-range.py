# 題目雖然看起來很難 Median 題，但其實很簡單。
# 數字在那裡跳動時，會有「固定不動」的位數。把它㫓找出來。
# 找出來後，再進位回去，就是答案。
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0 # 移了幾次啊？
        while left != right:
            left //= 2
            right //= 2
            shift += 1 # +1
        return left << shift # 再還原囉！

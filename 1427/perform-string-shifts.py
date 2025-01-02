# LeetCode 1427. Perform String Shifts
# 字串 s ，請照 shift[i] 裡，會有「運行方向」（0向左、1向右）及「移動量」改變字串
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        head = 0  # 記錄「最終」的移動量的「頭」
        for d, a in shift:  # direction, amount
            # 先照著 direction 和 amount 模擬「轉動的效果」
            if d==0: head += a  # 向左移動，等於「開頭」的是「往右」的
            else: head -= a  # 向右移動，等於「開頭」的是「往左」的
        N = len(s)
        head = ((head%N)+N)%N  # 把 head 換算成 0...N 之間的整數值
        return s[head:] + s[:head]  # 就從「頭」開始，再接上「後面那段」

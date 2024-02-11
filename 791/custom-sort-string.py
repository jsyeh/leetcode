# 將 s 裡的字母，照 order 的順序排序
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = list(s)
        # 因字串無法 .sort()，所以 s = list(s) 先轉成 list
        s.sort(key=lambda c: order.index(c) if c in order else -1)
        # 本來我是寫 s.sort(key=lambda c: order.index(c)) 但有些c不在order裡
        # 所以我寫得長一點：如果 c in order 就把 index 找出來用，不然就-1隨便放
        return ''.join(s)

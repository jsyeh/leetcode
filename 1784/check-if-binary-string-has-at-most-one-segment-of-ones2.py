# LeetCode 1784. Check if Binary String Has at Most One Segment of Ones
# 確認「字串 s 裡的 1 都聚在一起」
# 「最多只能有1堆」的 ones。若有第2堆ones的話，就False
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        prev = '1'  # 「前一項」，一開始是'1'
        for c in s:  # 每個字母逐一比較
        # 一開始是'1'，如果變成'0'後，又變成 '1' 就失敗。
            if prev=='0' and c=='1':
                return False  # 由 '0' 變成 '1' 失敗
            prev = c  # 更新「前一項」
        return True # 沒有失敗，就成功

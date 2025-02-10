# LeetCode 3174. Clear Digits
# 從左到右，每次可把「數字」及它左邊的「字母」一起刪除，照著模擬即可
class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []  # 利用 list 來放答案
        for c in s:  # 每次挑1個字 c 來判妡
            if c.isdigit():
                ans.pop()  # 「數字」的左邊是「字母」，就吐掉
            else:  # 沒辦法吐掉
                ans.append(c)  # 就把新字母加進去
        return ''.join(ans)

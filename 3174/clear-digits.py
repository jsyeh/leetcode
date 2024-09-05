# LeetCode 3174. Clear Digits
# 把「第1個digit及其左邊的non-digit刪除」
class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        for i, c in enumerate(s):
            # 要取出 ans[-1] 所以要檢查 len(ans)>0
            if len(ans)>0 and ans[-1].isalpha() and c.isdigit():
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)


# LeetCode 2138. Divide a String Into Groups of Size k
# s 字串，分成「每k個字母一群」，最後不足k個時，填入 fill 字母
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []  # 用來塞一堆字串（每段的長度都是k）
        for i in range(0, len(s), k):  # 「每k個字母一群」
            ans.append(s[i:i+k])  # 將 k 個字母塞入 ans
        if len(ans[-1]) != k:  # 如果答案的最後一群「不足k個」
            # 用 Python 字串 ljust() 補齊 k 項
            ans[-1] = ans[-1].ljust(k, fill)
        return ans

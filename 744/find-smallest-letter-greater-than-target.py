# LeetCode 744. Find Smallest Letter Greater Than Target
# 在 letters 字母的陣列裡，找比 target 字母大的最小字母
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]  # 如果找不到，就回傳 letters 的第1個字母
        letters.sort()  # 排序，以便逐一找答案
        for c in letters:  # 小到大，依序比較
            if c > target: return c  # 找到第1個比 target 大的字母，成功
        # 但如果都沒找到的話
        return ans  # 把一開始記起來的 letters[0] 拿來用

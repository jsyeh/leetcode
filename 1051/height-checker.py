# LeetCode 1051. Height Checker
# 又是開心的 Easy 題：每年拍照「量身高」，要從小到大站好。
# 不過一開始沒有排好，問有幾個人要「調位置」才行
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)  # 最後「希望」排好的位置
        ans = 0
        for i in range(len(heights)):  # 逐一比較，看位置對不對
            if expected[i] != heights[i]:  # 如果位置不對
                ans += 1  # 「調位子」的人 +1
        return ans

# LeetCode 1183. Maximum Number of Ones
# matrix 大小是 width * height，裡面每個 sideLength 平方的區塊「最多有 maxOnes」個1
# 請問 matrix 裡最多有幾個1？照著 Hint 實作，使用 greedy 的方法來解，照規則來「重覆」
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        counts = []  # 記錄「小正方形」裡，每個小格子的「出現次數」
        s = sideLength  # 為了讓程式碼短一點，換變數名
        # 先了解在「小正方形」裡，每個小格子在「大矩陣」裡出現幾次
        for i in range(sideLength):
            for j in range(sideLength):
                # 在 row 方向，重覆幾次
                row_count = height // s + (1 if i < height % s else 0)
                # 在 col 方向，重覆幾次
                col_count = width // s + (1 if j < width % s else 0)
                # 兩個相乘，便是「這個小格子」在「大矩陣」裡重覆出現的次數
                counts.append(row_count * col_count)
        # 每個小格子的「出現次數」，挑「最重要的 maxOnes 個小格子」即可
        counts.sort(reverse=True)  # 大到小排好
        return sum(counts[:maxOnes])  # 最大的 maxOnes 個小格子

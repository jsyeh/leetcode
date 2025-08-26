# LeetCode 3000. Maximum Area of Longest Diagonal Rectangle
# 有很多長方形的 [長,寬] 資訊，問「對角線」最長的那個長方形的「最大面積」
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDD = 0  # 目前最長的「對角線」的平方（根據畢氏定理，就 L*L+W*W 的值）
        ans = 0  # 對應的答案（面積）
        for L, W in dimensions:  # 針對「每個長方形」的「長寬」
            if L*L + W*W > maxDD:  # 對角線更長的話
                maxDD = L*L + W*W  # 更新「對角線」的平方
                ans = L*W  # 更新答案（面積）
            elif L*L + W*W == maxDD:  # 「對角線」若長度相同
                ans = max(ans, L*W)  # 更新「最大的面積」
        return ans

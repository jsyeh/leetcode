# LeetCode 3021. Alice and Bob Playing Flower Game
# 題目描述不容易理解：兩條路的花朵數 1 <= x <= n 和 1 <= y <= m
# A B 輪流「2條路挑1條」走取走1朵花，花全摘光，就得勝
# 有幾種可能的花的x,y分佈狀況，能讓先走的 Alice 一定得勝？
# 題目寫得很複雜，答案卻很簡單：x+y是奇數，就可以了。
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # x 是偶數的可能有 n // 2 種，剩下是奇數的可能
        # y 是偶數的可能有 m // 2 種，剩下是偶數的可能
        # 所以答案=「x偶數配y奇數」+「y奇數配x偶數」
        # = xEven * (m-yEven) + (n-xEven) * yEven
        xEven = n // 2  # x偶數，剩下的 x奇數是 n - xEven
        yEven = m // 2  # y偶數，剩下的 y奇數是 m - yEven
        return xEven * (m-yEven) + (n-xEven) * yEven

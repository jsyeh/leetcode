# LeetCode 3024. Type of Triangle
# 正三角形、等腰三角形、任意三角形、無法組成三角形
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)  # 先把3個邊「小到大」排好
        if a+b<=c: return "none"  # 無法組成三角形
        if a==b and b==c: return "equilateral"  # 正三角形
        if a==b or b==c: return "isosceles"  # 等腰三角形
        return "scalene"  # 任意三角形

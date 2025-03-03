# LeetCode 2161. Partition Array According to Given Pivot
# 給 pivot，小的放左邊、大的放右邊、相同的放中間，順序要保持。
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, middle, right = [], [], []
        for num in nums:
            if num < pivot: left.append(num)  # 小的放左邊
            elif num > pivot: right.append(num)  # 大的放右邊
            else: middle.append(num)  # 相同的放中間
        return left + middle + right

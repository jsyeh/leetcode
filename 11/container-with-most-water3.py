# LeetCode 11. Container With Most Water
# 陣列代表「直線的高度」，任挑2條直線，問長方形區域水「最多」能裝多少？
# 能裝多少水，由左右的寬度、左右的高度來決定。所以從「最左、最右」出發
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            ans = max(ans, min(height[left],height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

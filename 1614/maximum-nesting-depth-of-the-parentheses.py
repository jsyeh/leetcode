# LeetCode 1614. Maximum Nesting Depth of the Parentheses
# 找出「括號」最深有幾層。就照著字串讀取，即時修正層數 d
# 如果層數 d 比 ans 大，就更新 ans
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = d = 0
        for c in s:
            if c=='(': d += 1 # 遇到上括號，層數+1
            if c==')': d -= 1 # 遇到下括號，層數-1
            ans = max(ans, d) # ans 更新為最大的層數
        return ans

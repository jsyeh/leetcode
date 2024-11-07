# LeetCode 2275. Largest Combination With Bitwise AND Greater Than Zero
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0  #  迴圈前面 ans = 0
        for i in range(24):  # 針對每個 bit 可能的位置
            bit = 1<<i  # 製作出對應的 bit
            count = 0
            for now in candidates:  # 針對每個數字，比對「對應 bit」
                if now & bit > 0:  # 如果有對應 bit
                    count += 1  # 就多投1票
            ans = max(ans, count)  # 迴圈中間更新 ans
        return ans  # 迴圈後面 ans 拿來用

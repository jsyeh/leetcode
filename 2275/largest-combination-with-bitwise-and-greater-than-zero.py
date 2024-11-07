# LeetCode 2275. Largest Combination With Bitwise AND Greater Than Zero
# 最多能有幾個數的 Bitwise AND 計算後「不會是0」
# 數字最多有 10^5 所以不能用暴力兩層 for 迴圈。
# Hint 2 說, 數字最大 10^7 約 24 bits, 就針對每個 bit 看最多有幾個數
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [1]  # 從 1 開始, 要建出 1,2,4,8,16,32,...
        for i in range(24):
            bits.append(bits[-1]*2)  # 做出 每個 bit
        
        ans = 0
        for bit in bits:  # 針對每個bit
            count = 0
            for now in candidates:
                if now & bit > 0:  # 有這個bit, 算同一國的
                    count += 1
            ans = max(ans, count)  # 更新 ans
        return ans

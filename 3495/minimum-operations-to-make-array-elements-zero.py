# LeetCode 3495. Minimum Operations to Make Array Elements Zero
# queries 給多組範圍，每組 [L,R] 對應 [L, L+1, ... R] 的陣列，每次挑2數變1//4的整數，需幾次可全變成0
# 看似簡單，但數字太多、數字太大，不能「暴力模擬」。需要數學化簡：每次變1/4，像取log
# Hint 1 解釋「x變成0」需要次數是 floor(log4(x))+1
# Vlad 示範 [1..3] [4..15] [16..63] [64..255] 分區間，即 4^n 到 4^(n+1)-1
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0  # 累積每一段需要的次數
        for L, R in queries:  # 每一段都去試
            now = 0  # 這一段的範圍 L...R 需要走幾步？
            steps, p4 = 1, 1  # steps 要走幾步、p4 對應 pow of 4, 4的很多次方
            while p4 <= R:  # pow of 4, 4的很多次方 vs. 右邊界
                PL = max(L, p4)  # 左邊界 （本p4區間有幾個數？ [左邊界...右邊界]）
                PR = min(R, p4*4-1)  # 右邊界（本區間有幾個數： (PR-PL+1)
                now += max(0, (PR-PL+1)*steps)  # 有幾個數要走 steps 步
                steps += 1  # 走幾步 走p步
                p4 *= 4  # 4的很多次方
            ans += (now+1) // 2  # 每次挑2個數字，所以 // 2 即可，但單數就再+1
        return ans

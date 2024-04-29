# 想知道 start 要幾過幾次 bit flip 才能變成 goal
# 這題用到了 XOR 的觀念：只要 XOR 後，就知道兩數「差幾次bit flip」
# 再使用「剝皮法」便能知道「有幾個bit是1」也就是需要 bit flip 的次數
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        now = start ^ goal  # XOR 看「差幾個bit」
        ans = 0
        while now > 0:  # 剝皮法
            ans += now % 2
            now //= 2
        return ans


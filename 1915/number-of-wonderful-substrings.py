# 只能有1個字母「出現奇數次」，總共有多少 Wonderful Substrings
# 用 DP 可解。總共只有10種字母 'a'...'j'，合格的substring是全部偶數，
# 或是 'a'...'j' 有一個是奇數。
# 我有點卡住，看了 votrubac 的解法，覺得很巧妙：利用 bit mask 來查表
# mask 對應 字母的奇偶狀況：10種字母，用了 bit 0...bit 9
# 利用 XOR 的性質，讓奇數次數的字母是1，偶數次數的字母會變回0
# table[mask] 對應 mask 字母奇偶狀況，之前「曾經出現幾次」
# mask 完全相同，代表「之前有個奇偶完全相同的位置」，相減，即是「全偶數」
# mask 變化 1個 bit，代表對應「只有1個奇數」的狀況
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        mask = 0
        table = [1] + [0] * 1023  # 10種字母，2^10=1024種可能的 bit mask
        # 最一開始 mask 0 出現1次。接下來開始逐字母統計
        for c in word:
            bit = 1 << (ord(c) - ord('a'))  # c字母對應的bit
            mask ^= bit  # 做 XOR，奇數次會是1，偶數次會變回0
            ans += table[mask]  # 如果之前出現過一樣的mask, 會對應「完美」的全偶數
            # 所以出現 table[mask] 幾次，答案就 += 次數
            for n in range(10):  # 'a'...'j' 有10種字母
                bit = 1 << n  # 某字母對應的bit
                ans += table[mask ^ bit]  # 剛好差1個字母，也是合理的，答案 += 次數
            table[mask] += 1  # 結束時，更新次數（這個 mask 又出現了1次）
        return ans


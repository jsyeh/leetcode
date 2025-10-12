# LeetCode 3539. Find Sum of Array Product of Magical Sequences
# 從陣列 nums 挑 m 個數（可重覆挑）希望 magical seq 剛好「2的seq次方」加起來，有 k 個 bit 1
# 把這 m 個數「乘起來」，再把全部可能的「乘起來」再加起來、再取餘數
# 靈感：可使用「排列組合」來算出「某一種排法」對應的 seq 所有排列組合方法，再乘起來
# 因 k <= m 代表「有些數字會重覆挑」bits 可能會「進位」
class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9+7  # 題目希望「取餘數」的質數
        # 總共有 60 個數，可用 bitmask 來了解「用了哪些數」包含「重覆使用」的「進位問題」
        @cache  # 用「函式呼叫函式」來解
        def helper(m, k, i, bitmask):  
            # 目前用了幾個數，對應「用了哪些數」的 bitmask
            if m<0 or k<0 or m + bitmask.bit_count() < k: 
                return 0  # 無法達成任務：m用盡、k用盡、剩下的1量不夠，都失敗
            if m==0:  # 順利把數湊齊，但bits對嗎？
                if k==bitmask.bit_count(): return 1 # 湊齊，很好！
                else: return 0  # 沒湊齊，失敗
            if i >= len(nums): return 0  # 超過終點，失敗
            ans = 0  # 開始累計：排列組合 * nums[i] 這個數「要用幾次」的答案 
            for take in range(m+1):  # 仿 KARAN AGNANI 的解法
                # 在 m 個數中，挑 take 個重覆的 nums[i] 來做用，有幾種可能（排列組合）
                ways = math.comb(m, take) * pow(nums[i], take, MOD) % MOD
                new_bitmask = bitmask + take  # 現在最低位「重覆取take個」對應的「進位狀況」
                ans += ways * helper(m-take, k - (new_bitmask%2), i+1, new_bitmask//2)
                # 開始累計：排列組合 * nums[i] 這個數「要用幾次」的答案 
                ans %= MOD
            return ans
        return helper(m, k, 0, 0)

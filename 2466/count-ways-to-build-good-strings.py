# LeetCode 2466. Count Ways To Build Good Strings
# 每次要加入 zero 個 '0' 或 one 個 '1'
# 有幾種方法，可建出「合規定」的字串（因數字太大，要 MOD 10**9+7）
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def helper(i):  # 利用「函式呼叫函式」來解決
            if i==high: return 1  # 剛好走到「上界」，成功
            if i>high: return 0  # 超過「上界」，失敗
            if i>=low:  # 有達到上界，已成功。且可再「往右長」
                return (1 + helper(i+one) + helper(i+zero)) % MOD
            return (helper(i+one) + helper(i+zero)) % MOD  # 還不夠，只能再「往右長」
        return helper(0)  # 用「函式呼叫函式」從頭開始測

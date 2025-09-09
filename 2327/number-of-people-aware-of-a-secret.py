# LeetCode 2327. Number of People Aware of a Secret
# 每個人可保密delay天，之後每天會告訴另1個人，直到第forget天後他就會「忘記秘密」
# 第1天，只有1人知道秘密。問n天後，有幾個人會知道/還記得秘密？
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9+7  # 因數字會變很大，題目要求取 10^9+7 的餘數
        @cache  # 用「函式呼叫函式」來解決問題
        def helper(d):  # 「某人」在第d天得知「秘密」
            if d + delay > n:  # 逾第n天，「某人」還在保密期間內
                return 1  # 這個狀況，到第n天時，就「某人」他1個人知道
            if d + forget > n: ans = 1  # 「某人」在第n天還沒忘記秘密
            else: ans = 0  # 「某人」在第n天已經忘記秘密
            # 不管最後有沒有忘記，接下來，從「某人」出發，可蔓延多少人？
            for dd in range(d+delay, min(n+1, d+forget)):  # 每個 dd 天，會多1個人知道、蔓延
                ans = (ans + helper(dd)) % MOD
            return ans
        
        return helper(1)  # 第1天，有1個人知道秘密，開始往後探索/蔓延
        

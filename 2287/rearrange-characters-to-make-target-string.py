# 左邊字串 s 裡，有多少組 target 所需的字母。字母不用連續。
# 最重要的是 "we cannot reuse the letter" 所以字母不能重覆用
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        N, N2 = len(s), len(target)
        if N < N2: return 0 # 長度不夠，提早結束

        d = defaultdict(int) # 左邊 s 的字母統計
        for c in s: # 先照右target字串長度
            d[c] += 1 # 統計目前字串(前幾個字母)字母統計
        
        d2 = defaultdict(int) # 右邊 target 的字母統計
        for c in target:
            d2[c] += 1 # 統計字母出現次數

        ans = inf # 開始統計「有幾組相同」
        for k in d2:
            if d2[k] != 0: # 不處理0的部分，避免 Divied by zero 除以0
                ans = min(ans, d[k] // d2[k])  # 每組看是幾倍
        return ans

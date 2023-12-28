# 查看 words 逐一連起來, 是否會與 s 相同
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        now = '' # 因 s 長度至少有1, 所以可以不用檢查空字串
        for w in words:
            now += w # 直接從 words[0] 開始測試, 再慢慢變長
            if now == s: return True
        return False

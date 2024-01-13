# Anagram 是「用的字母都相同」的字
# 題目想問：需要最少「幾步（換幾個字母）」可做出Anagram
# 也就是「看它們倆個」差幾個字母
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        H = defaultdict(int) # 字母 Histogram分布狀況
        for c in s:
            H[c] += 1 # 增加提供
        for c in t:
            H[c] -= 1 # 用掉就減掉

        diff = 0 # 兩個字串，有差幾個字（不同）
        for c in H: # 最後統計狀況
            diff += abs(H[c]) # 有負的，要絕對值
        return diff//2 # 換一個字、一來一往，要除2

# 想找 s 的 substring 裡, 剛好把1個字母換掉, 變成 t 的 substring
# 舉例子 s=computer, t=computation, 那有個 compute 和 computa 只差1字母
# 問有幾種可能的 substring 組合 (substring 的開始、結束點不同, 就視為是新的組合)
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        # 好像要用 DP但是我不會
        M, N = len(s), len(t)
        ans = 0
        for i in range(M):
            for j in range(N):
                length = 0
                miss = 0
                while i+length<M and j+length<N and miss<2:
                    # 沒超過字串的範圍, 且 miss 的次數還在1次以下, 就繼續做
                    if s[i+length] != t[j+length]: #對應位置的字母不相同
                        miss += 1
                    if miss==1: ans += 1 # 剛好 miss 1次的話, 符合題目要求
                    length += 1 # 長度慢慢增加
        return ans

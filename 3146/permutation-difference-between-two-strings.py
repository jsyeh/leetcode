# LeetCode 3146. Permutation Difference between Two Strings
# 總共只有26個小寫字母，有不同的排列方式 s 與 t 問它們的距離
# 也就是 字母在 s 和 t 對應的 index 距離，再加起來
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos = {}  # 用字典，來存 c 在 s 的 index
        for i,c in enumerate(s):
            pos[c] = i
        
        ans = 0
        for i,c in enumerate(t):  # 針對 t 裡的每個字母，
            ans += abs(i-pos[c])  # 在 s 及 t 的 index 相減
        return ans

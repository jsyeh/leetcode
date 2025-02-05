# LeetCode 1790. Check if One String Swap Can Make Strings Equal
# 字串 s1 最多「只調動2個字母」的位置，能不能變成 s2
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        N = len(s1)  # 題目保證 s1 s2 長度相同
        bad1, bad2 = [], []  # 裡面存「沒對到」的字母
        for i in range(N):
            if s1[i] != s2[i]:
                bad1.append(s1[i])
                bad2.append(s2[i])
        if len(bad1)==0:  # 兩字串「完全相同」，沒有「不同」
            return True  # 成功
        if len(bad1)==2 and set(bad1)==set(bad2): 
            return True  # 有2個字母不同，且剛好可對調（相同集合）
        return False  # 無法成功，就失敗

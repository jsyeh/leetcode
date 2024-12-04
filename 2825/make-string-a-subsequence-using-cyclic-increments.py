# LeetCode 2825. Make String a Subsequence Using Cyclic Increments
# str1 裡的字母，能不能配對出 str2 裡的字母 （配對是：相同 or +1）
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        N1, N2 = len(str1), len(str2)
        i, j = 0, 0  # str1[i] vs. str2[j]
        for i in range(N1):  # Hint 3 介紹，以 i 為主，能不能配對到 str2[j]
            c1, c2 = ord(str1[i])-ord('a'), ord(str2[j])-ord('a')  # 將字母轉成 0...25
            if c1==c2: j += 1  # 直接配對
            elif (c1+1)%26==c2: j += 1  # 循環的+1配對
            if j==N2: return True  # str2[j] 全部順利配對完
        return False

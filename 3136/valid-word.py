# LeetCode 3136. Valid Word
# 測試 word 符合 (1) 至少3字元 (2) 數字、英文大小寫 (3) 至少1母音 (4) 至少1子音
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False  # (1) 至少3字元
        vowel, consonant = 0, 0  # 母音、子音 的數目
        for c in word:
            if not c.isdigit() and not c.isalpha(): 
                return False  # (2) 數字、英文大小寫
            if c.isalpha():  # 遇到字母
                if c in "aeiouAEIOU":
                    vowel += 1  # (3) 至少1母音
                else:
                    consonant += 1  # (4) 至少1子音
        if vowel==0 or consonant==0:
            return False  #  (3) 至少1母音 (4) 至少1子音
        return True

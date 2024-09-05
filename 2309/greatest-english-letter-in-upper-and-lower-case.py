# LeetCode 2309. Greatest English Letter in Upper and Lower Case
# 「同時有大寫、小寫」的字母，找到最大的。
class Solution:
    def greatestLetter(self, s: str) -> str:
        counter = Counter(s)
        for i in range(25, -1, -1): # 從'Z'到'A'
            # 若「大小寫」都有出現過
            if counter[chr(ord('A')+i)]>0 and counter[chr(ord('a')+i)]>0:
                return chr(ord('A')+i)
        return ''  # 沒有找到答案

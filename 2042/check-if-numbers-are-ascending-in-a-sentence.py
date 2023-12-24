# 確認字串裡出現的數字，是遞增的
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split() # 先斷字
        prevN = 0 # 字串中「數字」是正整數，so「前個數」從0開始
        for token in s: # 句子裡，每個 word 叫 token
            if token.isdigit(): # 若是數字
                if int(token) > prevN: # 有遞增，很好
                    prevN = int(token) # 更新 prevN
                else: # 不幸，沒有遞增
                    return False # 就出錯、結束
        return True # 都沒出錯日，就是成功

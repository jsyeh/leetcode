# 要把word裡, ch 字母(包含)之前的字,反過來。
# 這題的關鍵, 是先找到 ch 在 word 裡是第幾個位置。
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i]==ch: # 找到 ch 所在的位置 pos
                word2 = word[i::-1] + word[i+1:]  # 前面反過, 後面照順序
                return word2
        return word

# sentence 前後不能有空格，字與中間會有1個空格
# 現在 s 裡「每個字的結尾」有1...9的字，請照數字重組
class Solution:
    def sortSentence(self, s: str) -> str:
        # 這次的寫法，想要「短而有力」，所以程式比較奇怪
        s = s.split() # 斷字, s[i][-1]會是 1...9 的順序

        # 照著 list s, 把每個元素 字尾數字、前面英文 
        # 重組出 words 裡面會有 i 及 word
        words = [ (si[-1], si[:-1]) for si in s]
        # 照著 前面的 i 排序
        words.sort()

        # 照i排序後，再拆開，只留下右邊的 word
        ans = [word for i,word in words]
        return ' '.join(ans) # 利用空格 ' ' 把句子組出來

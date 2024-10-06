# LeetCode 1813. Sentence Similarity III 兩句子「是否相似」，即只差「插入一段句子」
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()  # 斷字，比較以 word 為單位
        N1, N2 = len(words1), len(words2)  # 句子的長度（有幾個word ）
        i, j = 0, 0  # 左手i個字母、右手j個字母
        while i<N1 and i<N2 and words1[i]==words2[i]:  # 沒超過範圍，且左邊第i個字相同
            i += 1  # 在「左邊」又湊到一個相同的字
        while j<N1 and j<N2 and words1[N1-1-j]==words2[N2-1-j]:  # 沒超過範圍，且右邊第j個字相同
            j += 1  # 在「右邊」又湊到一個相同的字

        # 左右都處理好了，那檢查看看
        if i+j>=N1 or i+j>=N2: return True # 若（左右合起來）可湊出其中一個句子(長度夠)，就是「拆解成功」
        return False  # 沒成功，就失敗了
''' Test data
"My name is Haley"
"My Haley"
"of"
"A lot of words"
"Eating right now"
"Eating"
"CwFfRo regR"
"CwFfRo H regR"
"Luky"
"Lucccky"
"xD iP tqchblXgqvNVdi"
"FmtdCzv Gp YZf UYJ xD iP tqchblXgqvNVdi"
"A B C D B B"
"A B B"
```

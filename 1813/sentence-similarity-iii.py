# LeetCode 1813. Sentence Similarity III 兩句子「是否相似」，即只差「插入一段句子」
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()  # 斷字，比較以 word 為單位
        N1, N2 = len(words1), len(words2)  # 句子的長度（有幾個word ）
        if N1<N2: # 希望左長、右短。若反過來，就交換
            words1, words2 = words2, words1
            N1, N2 = N2, N1

        left, right = -1, N2  # 句子2 的更左邊、更右邊
        for i in range(N2):  # 左到右巡(以小字串為主)
            if words1[i] != words2[i]: break  # 不同，就斷開
            left = i  # 相同的話，登記起來
        for i in range(-1, -N2-1, -1):  # 右到左巡： -1,-2...-N2-1 全巡
            if words1[i] != words2[i]: break;  # 不同，就斷開
            right = i + N2  # 換算成 句子2 的 0...N2-1 的範圍
        if left+1<right: return False  # 至少還差1個字，代表合不起來
        return True

# LeetCode 953. Verifying an Alien Dictionary
# 外星人的 26 個字母順序「很奇怪」，在 order 裡，有它們的順序
# 請照這個順序來做「外星人words」的排序，看結果是否正確
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = {}  # 就做個「對照表」，把外星人的字母，變成 0-25的整數
        for i,c in enumerate(order):
            table[c] = i # 外星人的字母，會變成「對應的 index」
        # 下面這行超酷，可以把 words 裡，每個 word 都變成 「一堆字母的index」
        alienWords = [[table[c] for c in list(word)] for word in words]
        sortedWords = sorted(alienWords)  # 一堆整數，可以排序
        return sortedWords == alienWords  # 排序後的結果，與原本相同，就是題目在問的問題

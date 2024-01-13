# 剛好 move 1次 word1[i] vs. word2[j]
# 讓兩個字串「不同的字母數」相同
# 因長度 10^5 所以不能用暴力法
# 可先統計個數，再照greedy的規則來做
# 想到一堆規則，但是覺得這樣的程式不漂亮
# 來回最多差到2，最小差到0
# 差2的話，要把單獨的移過去，且不能重覆
# 差1的話

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        def changeAndEqual(c1,c2): # 拔c1，拔c2 交換後，是否合格
            if c1==c2: return len(counter1)==len(counter2) 
            # 挑一樣的字母交換，結果不變

            len1, len2 = 0, 0 # 「不同的字母」個數
            if c2 not in counter1: len1 += 1 # 插入有效益 +1
            if c1 not in counter2: len2 += 1 # 插入有效益 +1
            for c in counter1:
                if not (c==c1 and counter1[c]==1): # 沒有 減不見
                    len1 += 1
            for c in counter2:
                if not (c==c2 and counter2[c]==1): # 沒有 減不見
                    len2 += 1
            if len1==len2: print(len1, len2, c1, c2)
            return len1==len2
        for c1 in counter1: # 挑 c1 來交換
            for c2 in counter2: # 挑 c2 來交換
                # 探討「交換」有什麼效果？是否會相同？
                if changeAndEqual(c1,c2):
                    return True
        return False
# case 94/99: "aa", "ab"
# case 93/99: 滿滿的 e 滿滿的 e 交換任兩字母，還是會相同

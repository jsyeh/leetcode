# 兩字串close：交換2字母位置 or 將字母的值交換
# abcde -> aecdb 把 b e 交換位置
# aacabb -> bbcbaa 把 a b 的值交換
# 因為字的長度很長 10^5 不能用暴力法，也不知要怎麼暴力
# 可能與「統計字母出現次數」有關。只要把次數排序，即可
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2): return False
        # 長度不同，就不能可能成功

        H1 = defaultdict(int)
        H2 = defaultdict(int) # 統計字母出現次數
        for c in word1: H1[c] += 1
        for c in word2: H2[c] += 1
        # 前面統計，後面查看集合 & 次數排序
        key1 = {k for k in H1.keys()}
        key2 = {k for k in H2.keys()}
        if key1 != key2: return False
        # 統計的字母集合不同，也是失敗

        count1 = [v for v in H1.values()]
        count2 = [v for v in H2.values()]

        count1.sort()
        count2.sort()
        for i in range(len(count1)): # 小到大的個數不同，也失敗
            if count1[i]!=count2[i]: return False
        return True # 經過嚴格考驗，總算成功了
# case 131/153: "uau", "ssx" # 字母不同，也不行
# case 132/153: "abbzzca", "babzzcz" 
# aabbczz vs. bbzzzc

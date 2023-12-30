# almost equivalent 是每種字母出現次數都最多「差3個字母」
# 所以先逐字統計完，再看差別 <= 3 即可
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        H1 = defaultdict(int)
        for c in word1:
            H1[c] += 1
        H2 = defaultdict(int)
        for c in word2:
            H2[c] += 1
        # 接下來比較統計的結果
        for c in set(H1)|set(H2):
            if abs(H1[c]-H2[c]) > 3: return False
        # 都沒有失敗，就是成功
        return True
        

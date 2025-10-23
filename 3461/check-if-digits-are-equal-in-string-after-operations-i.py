# LeetCode 3461. Check If Digits Are Equal in String After Operations I
# 把字串裡「對應的每個位數」相鄰2數加起來、記下「個位數」
# 看有無機會變成「全部相同」的數，持續做，直到最後變成2個數為止。
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(map(int, list(s) ))  # 因為 list 比較容易「修改內容」
        while len(s)>2:  # 持續做，直到「變成2位數」
            bad = False  # 一開始還沒壞掉
            for i in range(len(s)-1):  # 相鄰加起來
                s[i] = (s[i] + s[i+1]) % 10  # 取10的餘數，記下「個位數」
                if s[i] != s[0]: bad = True
            if not bad: return True
            s.pop()  # 吐掉最後的數（長度逐漸減少）
        return False

# 這題超簡單：對角對稱的矩陣。如果字不夠長，就不要看它。
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        N = len(words)
        for i in range(N):
            N2 = len(words[i]) # 因每個字的長度可能不同
            for j in range(N2): # words[i][j]一定有
                # 但 words[j][i] 要測長度
                # 列出不合格的條件:列不夠 or 不夠長 or 不相等
                if N<=j or len(words[j])<=i or words[i][j] != words[j][i]:
                    return False
        return True
# case 15/35: ["abc","b"]

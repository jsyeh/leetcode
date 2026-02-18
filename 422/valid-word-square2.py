# LeetCode 422. Valid Word Square
# 對角對稱的矩陣。如果字不夠長，就不要看它。
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j>=len(words) or i>= len(words[j]) or words[i][j] != words[j][i]:
                    # 要比較 words[i][j] words[j][j]，但右邊 words[j][i] 可能不夠長
                    # 所以要先看 j 是否超過 words，再看 i 是否超過 words[j] 
                    return False
        return True

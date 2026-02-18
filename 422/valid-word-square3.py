# LeetCode 422. Valid Word Square
# 對角對稱的矩陣。如果字不夠長，就不要看它。
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # 用 zip_longest(*words) 取出 ranspose matrix (缺項會補None)
        words2 = tuple(zip_longest(*words))  # 先 transpose 過去
        words1 = tuple(zip_longest(*words2))  # 再 transpose 回來
        # 就可以比較兩個「變成長方形」的 matrix
        return words1 == words2

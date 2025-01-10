# LeetCode 916. Word Subsets
# 從 words1 挑出合格的字：這些字裡，有 words2的「每個字」的「全部字母」
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # 可善用 Python 的 Counter（是一種set），先收集 words 裡出現的「全部字母」
        words2set = Counter()  # 裡面放 words2「每個字」的「全部字母」的數目（最大值）
        for word in words2:
            words2set |= Counter(word)  # OR 剛好可以找到「最大的量」
        ans = []
        for word in words1: # 開始檢查「合格的字」
            if Counter(word) >= words2set:  # 「大於等於」，剛好就「合格」
                ans.append(word)
        return ans

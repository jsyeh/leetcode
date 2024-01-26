# 在 words1 words2 裡都「只出現1次」
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2) # 轉成 Counter()字典
        ans = 0
        for w in counter1:
            if w in counter2 and counter1[w]==1 and counter2[w]==1:
                ans += 1
                # print(w) # Debug 用
        return ans

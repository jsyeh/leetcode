# LeetCode 884. Uncommon Words from Two Sentences
# 找出「只」出現在 s1 或 s2 的字，而且只出現1次。
# 剛好就是「總共只出現1次」的字
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = Counter(s1.split()) + Counter(s2.split())
        ans = []
        for word in counter: # 合起來看，只出現1次的字，都是答案
            if counter[word]==1: ans.append(word)
        return ans


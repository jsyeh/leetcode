# 找出「只」出現在 s1 或 s2 的字
# 而且只出現1次
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        set1 = Counter(s1.split()) # 記得要先斷字
        set2 = Counter(s2.split())
        ans = []
        for w in set1:
            if set1[w]==1 and w not in set2: # 只在s1不在s2
                ans.append(w)
        for w in set2:
            if set2[w]==1 and w not in set1: # 只在s2不在s1
                ans.append(w)
        return ans

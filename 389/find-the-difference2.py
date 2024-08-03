class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = Counter(t) - Counter(s)  # 改用 Counter()簡化程式碼
        return list(ans.keys())[0]  # key只會有1個，所以轉成list後，取[0]

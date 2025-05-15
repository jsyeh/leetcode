# LeetCode 2900. Longest Unequal Adjacent Groups Subsequence I
# words[i] 對應的 Group 是 groups[i] 可能是 0 or 1
# 找出 groups 「交錯」的「最長」subsequence，就直接從第0個開始即可
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [0]  # 裡面放「index」，一定可以放「最前面」第0個
        for i in range(1, len(words)):  # 後面依序檢查
            if groups[ans[-1]] != groups[i]:  # 只要不同 group
                ans.append(i)  # 就可以加進去
        return [words[i] for i in ans]  # 再把 ans 裡的 i 抽出來，變成對應的 words[i] 即可

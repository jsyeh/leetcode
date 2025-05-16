# LeetCode 2901. Longest Unequal Adjacent Groups Subsequence II
# 找最長 subsequence 裡面「相鄰的項」groups不相同、words[i] words[j]長度相同、只差1字母
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hammingOne(i,j):
            if len(words[i]) != len(words[j]): return False
            diff = 0
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]: diff += 1
            return diff==1
        @cache
        def helper(k):  # words[0]...words[k] 可跳，但一定要有 words[k]
            ansN, ans = 0, []
            for i in range(k):
                if groups[i] != groups[k] and hammingOne(i,k):
                    now, nowlist = helper(i)
                    if now>ansN: ansN, ans = now, nowlist
            return ansN+1, ans + [words[k]]
        ansN, ans = 1, [words[0]]
        for i in range(1, len(words)):
            now, nowlist = helper(i)
            if now>ansN: ansN, ans = now, nowlist
        return ans

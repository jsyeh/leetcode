# LeetCode 1858. Longest Word With All Prefixes
# words 裡「有一堆prefix」，找這些prefix「全部符合」的最長的字
class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ''
        prefixSet = set(words)  # 可先建 prefixSet
        for word in words:  # 再將 words 再檢測一次。
            bad = False  # 一開始還沒有「壞掉」
            prefix = ''  # 逐一檢查 word 的 prefix 都在 prefixSet
            for c in word:
                prefix += c
                if prefix not in prefixSet:
                    bad = True  # 不幸壞掉了
                    break
            if not bad:  # 是合法的字
                if len(word) > len(ans) or (len(word)==len(ans) and word < ans):
                    ans = word
        return ans


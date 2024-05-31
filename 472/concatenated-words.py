class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)

        @cache
        def dfs(word):
            for i in range(1,len(word)):  # 各種斷字方式
                part1 = word[:i]
                part2 = word[i:]
                if part1 in d and part2 in d:  # 簡單2個字
                    return True
                if part1 in d and dfs(part2):  # 右邊再拆
                    return True
                if part2 in d and dfs(part1):  # 左邊再拆
                    return True
            return False  # 都沒辦法斷字成功的話，失敗

        ans = []
        for word in words:
            if dfs(word):
                ans.append(word)
        return ans
# case 42/43: 超級多的字

# startWords[i] 反 targetWords[j] 裡的字母不重覆
# 問「有幾個字」可從 startWords 裡的字「變出來」
# 變出來的方法：(1)加個字母，再 (2) 任意調整順序
# 但 targetWords 及 startWords 都有 5*10^4 不能暴力試
# 用 hashmap 可快速找出「有沒有出現過」某些字
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start = set()
        for word in startWords:
            start.add(''.join(sorted(word))) # 字母排好序，有全部的 startWords
        print(start)
        ans = 0
        for word in targetWords: # 逐字去測
            for i in range(len(word)): # 每個字母都「減看看」
                if ''.join(sorted(word[:i]+word[i+1:])) in start:
                    # 減掉 word[i] 字母後的字，有在 start 出現過
                    ans += 1 # 就是「變得出來」
                    break
        return ans

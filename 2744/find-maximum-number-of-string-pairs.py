# 如果 words[i] == reversed(words[j]) 就是 paired
# 問最多有幾個 pairs
# 因為 words 裡每個字「都不同」，可暴力「正反」都放進set()
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set()
        ans = 0
        for word in words:
            if word in s: # 有出現過的話
                ans += 1 # 多一組 pair
            else: # 若沒出現過
                s.add(word) # 就把正的、反的，都加入 set
                s.add(word[::-1]) # 這是反過來的字串哦
        return ans

# 字母出現多次。但哪個字母「先出現第2次」
# 我是想到用字典。不過有人使用 set() 會更快。
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = defaultdict(int) # 利用字典，來存「出現次數」
        for c in s:
            count[c] += 1 # 字母 c 出現「多一次」
            if count[c]==2: return c # 如果達到「第二次」就可

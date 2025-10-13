# LeetCode 2273. Find Resultant Array After Removing Anagrams
# 將 words「相鄰的 anagrams（用相同字母）」移掉後面那個，直到「找不到相鄰 anagrams 為止」
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []  # 利用 Stack 反過來放、再「末位」檢查能否「對消」
        while len(words):  # 只要 words 還有剩
            stack.append(words.pop())  # 就吐一個給 Stack
            while stack and words and Counter(stack[-1])==Counter(words[-1]):
                stack.pop()  # 可「末位」對消，就吐掉後面的（已移到stack裡)
        return stack[::-1]  # 再反過來「放回」即時答案

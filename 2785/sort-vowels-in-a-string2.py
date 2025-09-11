# LeetCode 2785. Sort Vowels in a String
# s 字串裡「子音不要動」「母音要排序、再放回去」
# 這題超簡單，收集好母音、把母音排序好，再塞回字串裡
class Solution:
    def sortVowels(self, s: str) -> str:
        vowelSet = set("aeiouAEIOU")  # 母音對照表，用set()加速比對
        vowel = []  # 放字串 s 裡所有出現過的母音清單
        for c in s:  # 針對每一個字母檢查
            if c in vowelSet:  # 如果是母音
                vowel.append(c)  # 就加到 vowel 裡
        vowel.sort(reverse=True)  # 「倒過來排序」，之後 pop()取用最右邊「最小的」
        ans = []  # 每個字母塞到答案中
        for c in s:
            if c in vowelSet:  # 是母音
                ans.append(vowel.pop())  # 塞入「排序好的母音」最右邊「最小的」
            else:  # 否則
                ans.append(c)  # 塞入子音c
        return ''.join(ans)  # 把 list 合併成 字串

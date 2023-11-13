# 這題超簡單，收集好母音、把母音照順序排好，再塞回字串裡
class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = [] # 母音vowel的 list 裡，會收集 s 的全部母音
        def isVowel(c) -> bool: # 寫個函式，幫忙判斷是否為母音
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
                return True
            return False

        for c in s: # 針對每一個字母檢查
            if isVowel(c): # 如果是母音
                vowel.append(c) # 就加到 vowel 裡
        vowel.sort() # 把母音照順序排好
        ans = [] # 每個字母塞到答案中
        i = 0 # 利用 i 來取用 vowel[i]
        for c in s:
            if isVowel(c): # 原字串裡的母音
                ans.append(vowel[i]) # 就塞「排序好的母音」
                i += 1
            else:
                ans.append(c) # 否則，就直接塞入子音c
        return ''.join(ans) # 把 list 合併成 字串

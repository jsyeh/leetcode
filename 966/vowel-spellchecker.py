# LeetCode 966. Vowel Spellchecker
# 給一堆單字 wordlist 當依據，將 queries 裡的字，變成「正確的單字」
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        N = len(wordlist)  # wordlist 有 N 個字
        # 第0種：一模一樣的字
        type0 = {wordlist[i]:i for i in range(N)}  # 一模一樣的字
        # 第1種：只有「大小寫拼錯」(要第1個符合的字，所以用「倒過來的迴圈」左邊蓋掉右邊)
        type1 = {wordlist[i].lower():i for i in range(N-1,-1,-1)}  # 列出小寫
        # 第2箽：只有「母音拼錯」子音都拼正確(要第1個符合的字，還是用「倒過來的迴圈」)
        vowelSet = set('aeiou')  # 用 set() 快速找母音
        def vowelA(word):  # 變成小寫、再把「母音變成A」
            ans = []
            for c in word.lower():  # 都變成「小寫」，可避開「大小寫」問題
                if c in vowelSet: ans.append('A')  # 母音變成 'A'
                else: ans.append(c)  # 子音「照著放」
            return ''.join(ans)  # 變回「字串」
        type2 = {vowelA(wordlist[i]):i for i in range(N-1,-1,-1)}  # 倒過來的迴圈
        ans = []
        for w in queries:  # 接下來逐一解題
            if w in type0:  # 直接符合
                ans.append(wordlist[type0[w]])
            elif w.lower() in type1:  # 變成小寫後，符合
                ans.append(wordlist[type1[w.lower()]])
            elif vowelA(w) in type2:  # 變成小寫、再把「母音變成A」後，符合
                ans.append(wordlist[type2[vowelA(w)]])
            else: ans.append('')  # 找不到符合的字，放空字串
        return ans

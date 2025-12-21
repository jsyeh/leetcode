# LeetCode 966. Vowel Spellchecker
# 給一堆單字 wordlist 當依據，將 queries 裡的字，變成「正確的單字」
# 把 queries[i] 變成 wordlist 裡「正確的字」
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        table0 = set(wordlist)  # exact the same
        table1 = {} #defaultdict(str)  # case insenstive
        table2 = defaultdict(str)  # vowel ignore
        def ignoreVowel(word):
            now = ''
            for c in word.lower():
                if c in vowel: now += '*'
                else: now += c
            return now

        vowel = set("aeiou")
        for word in wordlist:
            if word.lower() not in table1:  # 沒用過
                table1[word.lower()] = word
            if ignoreVowel(word) not in table2:
                table2[ignoreVowel(word)] = word
        ans = []
        for word in queries:
            if word in table0: ans.append(word)
            elif word.lower() in table1: ans.append(table1[word.lower()])
            else: ans.append(table2[ignoreVowel(word)])
        return ans

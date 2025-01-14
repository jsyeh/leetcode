# LeetCode 2047. Number of Valid Words in a Sentence
# 字串 sentence 裡，用「空格」隔開許多 words，有幾個合法的字？
# 合法字的規則：(1) 只有字母、連字號、標點符號，不能有數字 
# (2) 連字號的左右必須有字母
# (3) 最多只能有1個標點符號(!,.)，放在字的最後面
class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        ans = 0
        for word in words:
            if re.search("\d", word): # 先解決數字問題
                continue  # 避開「有找到數字」
            if re.search("[^a-z]-", word) or re.search("-[^a-z]", word): # 減號的開頭、結尾有錯
                print(word, '-')
                continue
            if not re.search("^[a-z]*[!.,]*$", word) and not re.search("[a-z]-[a-z]", word):  # 「不是」字母開頭/合法標點符號結尾 （ . 也是答案）
                print(word, '^$')
                continue  # 避開
            if re.search("[!.,]", word[:-1]):  # 字中間有標點符號
                continue  # 避開
            if len(re.findall('-', word))>1: # 很多個減號
                continue
            if re.search("^-", word):  # 字首有減號
                continue  # 避開
            print(word, 'good')

            ans += 1
        return ans
